"""
Rule-based NLP preprocessor.
Extracts signals from raw message text using regex patterns before AI analysis.
"""

import re
from typing import Any, List


# Compiled patterns for performance
_URL_RE = re.compile(
    r"https?://[^\s\"'<>]+|www\.[^\s\"'<>]+|[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?",
    re.IGNORECASE,
)
_EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
_PHONE_RE = re.compile(r"(?:\+91[\s\-]?)?[6-9]\d{9}|(?:\+\d{1,3}[\s\-]?)?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}")
_MONEY_RE = re.compile(r"(?:₹|Rs\.?|INR|USD|\$)\s?\d+(?:,\d{3})*(?:\.\d{1,2})?|\d+(?:,\d{3})*\s?(?:₹|Rs\.?|rupees?)", re.IGNORECASE)
_OTP_RE = re.compile(r"\bOTP\b|\bone[\s-]?time[\s-]?password\b|\bverification code\b", re.IGNORECASE)
_APK_RE = re.compile(r"\.apk\b|install.*app|download.*file|\.exe\b", re.IGNORECASE)

_URGENCY_PHRASES = [
    r"\burgent\b", r"\bimmediately\b", r"\btoday\b", r"\bright now\b",
    r"\bact now\b", r"\bexpires?\b", r"\bdeadline\b", r"\blast chance\b",
    r"\bsuspended?\b", r"\bblocked?\b", r"\bclose[ds]?\b",
    r"\bwithin \d+ hours?\b", r"\bwithin \d+ minutes?\b",
    r"\bdo not delay\b", r"\bfailure to\b", r"\bwill be terminated\b",
]

_CREDENTIAL_PHRASES = [
    r"\bpassword\b", r"\bpin\b", r"\bcredentials?\b",
    r"\bverify your account\b", r"\bconfirm your account\b",
    r"\benter your\b", r"\bprovide your\b", r"\bsubmit your\b",
    r"\bbank details?\b", r"\baccount number\b", r"\bcvv\b",
]

_PAYMENT_PHRASES = [
    r"\bpay\b", r"\bpayment\b", r"\bregistration fee\b",
    r"\bprocessing fee\b", r"\bsecurity deposit\b",
    r"\btransfer\b", r"\bwallet\b", r"\brecharge\b",
]

_PRIZE_PHRASES = [
    r"\bcongratulations\b", r"\byou (have been|are) selected\b",
    r"\byou (have )?won\b", r"\blucky winner\b",
    r"\bprize\b", r"\breward\b", r"\bgift\b",
]

_IMPERSONATION_ORGS = [
    "sbi", "hdfc", "icici", "axis bank", "rbi", "irdai",
    "amazon", "flipkart", "google", "microsoft", "apple",
    "myntra", "meesho", "zepto", "swiggy", "zomato",
    "india post", "bluedart", "delhivery", "fedex", "dtdc",
    "police", "cbi", "income tax", "epfo", "aadhaar", "uidai",
    "trai", "bsnl", "jio", "airtel",
]


def _match_patterns(text: str, patterns: List[str]) -> List[str]:
    matches = []
    for pattern in patterns:
        found = re.findall(pattern, text, re.IGNORECASE)
        if found:
            matches.extend(found if isinstance(found[0], str) else [m[0] for m in found])
    return list(set(matches))


def preprocess(message: str) -> dict:
    """
    Run deterministic extraction on a raw message.
    Returns a structured dict of detected signals.
    """
    text = message.strip()
    lower = text.lower()

    urls = _URL_RE.findall(text)
    emails = _EMAIL_RE.findall(text)
    phones = _PHONE_RE.findall(text)
    money = _MONEY_RE.findall(text)
    has_otp = bool(_OTP_RE.search(text))
    has_apk = bool(_APK_RE.search(text))

    urgency_signals = _match_patterns(text, _URGENCY_PHRASES)
    credential_signals = _match_patterns(text, _CREDENTIAL_PHRASES)
    payment_signals = _match_patterns(text, _PAYMENT_PHRASES)
    prize_signals = _match_patterns(text, _PRIZE_PHRASES)

    mentioned_orgs = [org for org in _IMPERSONATION_ORGS if org in lower]

    # Compute a rough signal score to guide AI
    signal_score = (
        len(urgency_signals) * 2
        + len(credential_signals) * 3
        + len(urls) * 1
        + len(money) * 2
        + (3 if has_otp else 0)
        + (4 if has_apk else 0)
        + len(payment_signals) * 2
        + len(prize_signals) * 1
        + len(mentioned_orgs) * 1
    )

    return {
        "urls": urls,
        "emails": emails,
        "phones": phones,
        "money": money,
        "has_otp_reference": has_otp,
        "has_apk_or_executable": has_apk,
        "urgency_signals": urgency_signals,
        "credential_signals": credential_signals,
        "payment_signals": payment_signals,
        "prize_signals": prize_signals,
        "mentioned_organizations": mentioned_orgs,
        "signal_score": signal_score,
        "message_length": len(text),
    }
