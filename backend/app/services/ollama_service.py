import json
import os
import re
import httpx
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_ENABLED = os.getenv("OLLAMA_ENABLED", "true").lower() == "true"

_ANALYZE_PROMPT = """You are the language interpretation component of CyberGuard, a cybersecurity awareness application.
Analyze the supplied message only as text.
Identify the likely communication intent and security category.
Do not claim certainty that a message is malicious.
Do not invent URLs, entities, organizations, evidence or facts.
Do not calculate or invent the final risk score.
Return valid JSON only.

Message:
{message}

Entities:
{entities}

Indicators:
{indicators}

Risk Score:
{risk_score}

Return ONLY a valid JSON object with this exact structure:
{{
  "intent": "Brief label for the detected intent (e.g. 'Credential Verification', 'Payment Fraud', 'Informational')",
  "category": "Refined category based on indicators (e.g. Potential Phishing, Job Scam, Delivery Scam)",
  "explanation": "2-3 sentences explaining the assessment based on provided facts",
  "follow_up_answer": "An initial recommended action based on the facts"
}}"""


_CHAT_PROMPT = """You are CyberGuard, a cybersecurity assistant. The user has analyzed a message and is asking a follow-up question.

Current analysis context:
Category: {category}
Risk Score: {risk_score}
Intent: {intent}
Explanation: {explanation}
Indicators: {indicators}

Previous question/responses (if any):
{chat_history}

User question: {question}

Provide a clear, helpful, and accurate answer in 2-4 sentences. Use professional but accessible language.
Do not invent information not supported by the analysis. Focus on being genuinely useful.
Do not use markdown formatting in your response. Return plain text."""

async def check_status() -> Dict[str, Any]:
    if not OLLAMA_ENABLED:
        return {"available": False, "model": None}
    
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/version")
            if response.status_code == 200:
                return {"available": True, "model": OLLAMA_MODEL}
    except Exception:
        pass
    
    return {"available": False, "model": None}

def _extract_json(text: str) -> dict:
    """Extract JSON from model response, handling markdown fences."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```\s*$", "", text, flags=re.MULTILINE)
    
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")

async def analyze_message(message: str, entities: list, indicators: list, risk_score: int) -> Optional[Dict[str, Any]]:
    if not OLLAMA_ENABLED:
        return None
        
    prompt = _ANALYZE_PROMPT.format(
        message=message,
        entities=json.dumps(entities),
        indicators=json.dumps(indicators),
        risk_score=risk_score
    )
    
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "format": "json"
                }
            )
            response.raise_for_status()
            data = response.json()
            return _extract_json(data.get("response", "{}"))
    except Exception as e:
        print(f"Ollama analyze failed: {e}")
        return None

async def chat_response(question: str, context: dict) -> Optional[str]:
    if not OLLAMA_ENABLED:
        return None
        
    indicators_text = "; ".join(
        ind.get("name", "") for ind in context.get("indicators", [])
    ) or "None detected"
    
    prompt = _CHAT_PROMPT.format(
        category=context.get("category", "Unknown"),
        risk_score=context.get("risk_score", "Unknown"),
        intent=context.get("intent", "Unknown"),
        explanation=context.get("explanation", ""),
        indicators=indicators_text,
        chat_history="", # Could be expanded to include actual history if provided
        question=question,
    )
    
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()
    except Exception as e:
        print(f"Ollama chat failed: {e}")
        return None
