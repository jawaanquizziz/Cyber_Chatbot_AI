"""
Gemini API service using the google-genai SDK (Python 3.14 compatible).
Falls back gracefully when the API key is not configured.
"""

import json
import os
import re

from dotenv import load_dotenv

load_dotenv()

_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
_CONFIGURED = bool(_API_KEY)
_client = None

if _CONFIGURED:
    try:
        from google import genai
        _client = genai.Client(api_key=_API_KEY)
    except Exception:
        _CONFIGURED = False


def is_configured() -> bool:
    return _CONFIGURED


_ANALYZE_PROMPT = """You are CyberGuard, a cybersecurity analysis assistant. Analyze the message below and return a structured JSON assessment.

Message:
{message}

Preprocessed signals (use to inform your analysis):
{signals}

Return ONLY a valid JSON object with this exact structure:
{{
  "category": "One of: Potential Phishing, Job Scam, Delivery Scam, Banking Scam, Malware Distribution, Investment Scam, Impersonation, Social Engineering, No Significant Threat Detected",
  "risk_level": "LOW, MEDIUM, or HIGH",
  "intent": "Brief label for the detected intent (e.g. 'Credential Theft', 'Payment Fraud', 'Informational')",
  "intent_explanation": "2-3 sentences explaining the inferred intent",
  "entities": [
    {{"type": "entity type (e.g. Organization, URL, OTP, Requested Information, Action, Money, Date, Phone)", "value": "the extracted value"}}
  ],
  "indicators": [
    {{"name": "Indicator name (e.g. Urgency, OTP Request, Suspicious URL)", "explanation": "1-2 sentences explaining why this was flagged"}}
  ],
  "recommended_actions": ["Action 1", "Action 2", "Action 3"],
  "explanation": "2-3 sentence professional summary of the assessment"
}}

Rules:
- Only flag indicators actually present in the message. Do not invent threats.
- If the message appears benign, set risk_level to LOW and indicators to an empty array.
- Use careful, hedged language: "appears to", "may indicate", "commonly associated with".
- Never claim definitive proof of malicious intent.
- Entities array should only include items genuinely extractable from the message.
- Response must be valid JSON only. No markdown, no extra text."""


_CHAT_PROMPT = """You are CyberGuard, a cybersecurity assistant. The user has analyzed a message and is asking a follow-up question.

Current analysis context:
Category: {category}
Risk Level: {risk_level}
Intent: {intent}
Explanation: {explanation}
Indicators: {indicators}

User question: {question}

Provide a clear, helpful, and accurate answer in 2-4 sentences. Use professional but accessible language.
Do not invent information not supported by the analysis. Focus on being genuinely useful.
Do not use markdown formatting in your response."""


def _extract_json(text: str) -> dict:
    """Extract JSON from model response, handling markdown fences."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```\s*$", "", text, flags=re.MULTILINE)
    return json.loads(text.strip())


def _validate_response(data: dict) -> dict:
    """Ensure required fields exist with sane defaults."""
    defaults = {
        "category": "Unknown",
        "risk_level": "MEDIUM",
        "intent": "Unknown",
        "intent_explanation": "Analysis could not determine intent.",
        "entities": [],
        "indicators": [],
        "recommended_actions": ["Exercise caution with this message."],
        "explanation": "The analysis did not produce a complete result.",
    }
    for key, default in defaults.items():
        if key not in data or data[key] is None:
            data[key] = default
    data["risk_level"] = data["risk_level"].upper()
    if data["risk_level"] not in ("LOW", "MEDIUM", "HIGH"):
        data["risk_level"] = "MEDIUM"
    return data


async def analyze_message(message: str, preprocessed: dict) -> dict:
    """Run Gemini analysis on the message with preprocessed signal context."""
    if not _CONFIGURED or _client is None:
        raise RuntimeError("Gemini API key not configured")

    signals_summary = (
        f"URLs found: {preprocessed.get('urls', [])}\n"
        f"Has OTP reference: {preprocessed.get('has_otp_reference', False)}\n"
        f"Has APK/executable: {preprocessed.get('has_apk_or_executable', False)}\n"
        f"Urgency signals: {preprocessed.get('urgency_signals', [])}\n"
        f"Credential signals: {preprocessed.get('credential_signals', [])}\n"
        f"Payment signals: {preprocessed.get('payment_signals', [])}\n"
        f"Money mentioned: {preprocessed.get('money', [])}\n"
        f"Organizations mentioned: {preprocessed.get('mentioned_organizations', [])}\n"
        f"Signal score: {preprocessed.get('signal_score', 0)}"
    )

    prompt = _ANALYZE_PROMPT.format(message=message, signals=signals_summary)

    response = _client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    raw = response.text

    try:
        data = _extract_json(raw)
    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError(f"AI returned malformed JSON: {e}") from e

    return _validate_response(data)


async def chat_response(question: str, context: dict) -> str:
    """Generate a contextual follow-up answer using the current analysis."""
    if not _CONFIGURED or _client is None:
        raise RuntimeError("Gemini API key not configured")

    indicators_text = "; ".join(
        ind.get("name", "") for ind in context.get("indicators", [])
    ) or "None detected"

    prompt = _CHAT_PROMPT.format(
        category=context.get("category", "Unknown"),
        risk_level=context.get("risk_level", "Unknown"),
        intent=context.get("intent", "Unknown"),
        explanation=context.get("explanation", ""),
        indicators=indicators_text,
        question=question,
    )

    response = _client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()
