"""
Demo mode service.
Returns realistic, pre-defined analysis results when Gemini API is unavailable.
Used for offline demonstrations and as a fallback.
"""

DEMO_ANALYSES = {
    "banking": {
        "category": "Potential Phishing",
        "risk_level": "HIGH",
        "intent": "Credential / Account Verification",
        "intent_explanation": (
            "The sender is attempting to persuade the recipient to verify account credentials "
            "under threat of account suspension. This is a common phishing pattern used to "
            "harvest OTPs and login details."
        ),
        "entities": [
            {"type": "Urgency", "value": "Account suspended today"},
            {"type": "Action", "value": "Verify account immediately"},
            {"type": "Requested Information", "value": "OTP"},
            {"type": "URL", "value": "Suspicious link (not shown)"},
        ],
        "indicators": [
            {
                "name": "Urgency",
                "explanation": "The message pressures the recipient to act immediately to prevent account suspension.",
            },
            {
                "name": "Account Suspension Threat",
                "explanation": "Threatening account closure is a classic social engineering tactic to bypass rational thinking.",
            },
            {
                "name": "OTP Request",
                "explanation": "Legitimate banks never request OTPs via SMS links. OTPs should only be entered on the official app or website.",
            },
            {
                "name": "External Link",
                "explanation": "The message directs the recipient to an external URL rather than the bank's official domain.",
            },
        ],
        "recommended_actions": [
            "Do not click the link in the message.",
            "Do not enter your OTP or account credentials anywhere linked from this message.",
            "Contact your bank directly using the number on the back of your debit/credit card.",
            "Report the message to your bank's fraud helpline.",
            "If you have already shared credentials, change your password immediately and contact your bank.",
        ],
        "explanation": (
            "This message contains several signals commonly associated with phishing attempts. "
            "The combination of urgency, account suspension threat, a request for an OTP, and an "
            "external link are well-known indicators of credential harvesting attacks targeting "
            "banking customers. No legitimate bank will ask you to verify your account via an "
            "SMS link or share your OTP."
        ),
    },
    "job": {
        "category": "Job Scam",
        "risk_level": "HIGH",
        "intent": "Financial Fraud via Fake Employment",
        "intent_explanation": (
            "The sender is offering an unsolicited employment opportunity and requesting "
            "a registration fee. This is a standard advance-fee job scam pattern."
        ),
        "entities": [
            {"type": "Prize / Offer", "value": "Work-from-home position"},
            {"type": "Requested Payment", "value": "₹2,499 registration fee"},
            {"type": "Action", "value": "Pay to complete application"},
        ],
        "indicators": [
            {
                "name": "Unsolicited Job Offer",
                "explanation": "The recipient did not apply for this position. Legitimate employers do not send unsolicited job offers via SMS.",
            },
            {
                "name": "Registration Fee Request",
                "explanation": "Requesting payment from a job applicant is a defining characteristic of employment scams.",
            },
            {
                "name": "Unusual Payment Request",
                "explanation": "No legitimate employer requires candidates to pay to complete a job application.",
            },
        ],
        "recommended_actions": [
            "Do not pay the registration fee.",
            "Do not provide any personal or financial information.",
            "Verify the company's existence independently through official sources.",
            "Report the message at cybercrime.gov.in.",
        ],
        "explanation": (
            "Legitimate employers do not charge applicants a registration or processing fee. "
            "This message follows a well-documented job scam pattern: an unsolicited offer with "
            "an unusually straightforward opportunity, followed by a fee request before any "
            "real work begins."
        ),
    },
    "delivery": {
        "category": "Delivery Scam",
        "risk_level": "MEDIUM",
        "intent": "Payment Fraud via Fake Courier Notification",
        "intent_explanation": (
            "The sender is impersonating a courier service and requesting a small payment "
            "to manipulate the recipient into providing payment details."
        ),
        "entities": [
            {"type": "Requested Payment", "value": "₹49"},
            {"type": "Action", "value": "Pay to reschedule delivery"},
            {"type": "URL", "value": "Suspicious payment link"},
        ],
        "indicators": [
            {
                "name": "Suspicious URL",
                "explanation": "The message includes a link to make payment, which is not how legitimate courier services operate.",
            },
            {
                "name": "Unusual Payment Request",
                "explanation": "Legitimate courier services do not request payment via SMS links for redelivery.",
            },
            {
                "name": "Impersonation",
                "explanation": "The message impersonates a courier service to appear credible.",
            },
        ],
        "recommended_actions": [
            "Do not click the payment link.",
            "Check your actual order status through the official courier website using your tracking number.",
            "If you have a genuine delivery issue, contact the courier's official customer service.",
        ],
        "explanation": (
            "This message mimics a courier delivery failure notification and requests a small payment "
            "via a link. Real courier companies do not request redelivery fees through SMS links. "
            "The small amount is used to lower the recipient's guard."
        ),
    },
    "malware": {
        "category": "Malware Distribution",
        "risk_level": "HIGH",
        "intent": "Device Compromise via Malicious Application",
        "intent_explanation": (
            "The sender is attempting to get the recipient to install an application "
            "from an unofficial source, which is a primary method for distributing malware."
        ),
        "entities": [
            {"type": "File Type", "value": "APK (Android Application)"},
            {"type": "Action", "value": "Download and install"},
            {"type": "Claim", "value": "Shared document from a friend"},
        ],
        "indicators": [
            {
                "name": "Pressure to Install Software",
                "explanation": "The message requests installation of an APK from an external source, bypassing official app stores.",
            },
            {
                "name": "Unexpected Attachment",
                "explanation": "Legitimate services share documents through official apps, not via APK installations.",
            },
            {
                "name": "Impersonation",
                "explanation": "The message falsely claims to be from a known contact to build trust.",
            },
        ],
        "recommended_actions": [
            "Do not download the APK file.",
            "Do not install applications from sources outside the Google Play Store or Apple App Store.",
            "If you believe the message came from a known contact, verify with them through a separate communication channel.",
            "If you have already installed the file, consider running a device security scan and revoking app permissions.",
        ],
        "explanation": (
            "This message attempts to distribute malware by requesting the installation of an "
            "APK file from an external source. APKs distributed outside official app stores "
            "are a common vector for spyware, keyloggers, and banking trojans. Legitimate "
            "documents are not shared via APK files."
        ),
    },
    "benign": {
        "category": "No Significant Threat Detected",
        "risk_level": "LOW",
        "intent": "Informational Notification",
        "intent_explanation": (
            "The message appears to be a routine informational notification with no requests "
            "for personal information, payment, or action beyond awareness."
        ),
        "entities": [
            {"type": "Subject", "value": "College assignment"},
            {"type": "Date", "value": "Tomorrow at 5 PM"},
        ],
        "indicators": [],
        "recommended_actions": [
            "No action required from a security perspective.",
            "Verify the deadline through your college's official portal if in doubt.",
        ],
        "explanation": (
            "This message does not contain urgency tactics, requests for sensitive information, "
            "suspicious links, or payment demands. It appears to be a routine academic reminder. "
            "No significant threat indicators were detected."
        ),
    },
}

DEMO_CHAT_RESPONSES = {
    "why was this flagged": (
        "This message was flagged because it contains a combination of signals "
        "that are strongly associated with phishing attempts: urgent language designed "
        "to prevent careful thinking, a threat to your account, a request for an OTP "
        "(which no legitimate organization sends via SMS links), and an external URL. "
        "Individually, some signals might appear in legitimate messages, but their combination "
        "is a strong indicator of a phishing attempt."
    ),
    "what information is the sender trying to obtain": (
        "Based on the analysis, the sender appears to be trying to obtain your OTP "
        "(one-time password) and potentially your account login credentials. "
        "This information could be used to access your account and conduct unauthorized transactions."
    ),
    "what should i do next": (
        "The safest course of action is: do not interact with the link or any contact details "
        "in the message. If you are genuinely concerned about your account, call your bank's "
        "official customer care number (found on the back of your card or the bank's official website). "
        "Additionally, if you have already shared any credentials, change your password immediately "
        "and report the incident to your bank."
    ),
    "which part of the message is suspicious": (
        "Several parts of this message are suspicious: the word 'URGENT' creates artificial pressure, "
        "the threat of account suspension is used to provoke a reaction rather than allow careful thought, "
        "the request to 'enter your OTP' through a link is a hallmark of credential harvesting, "
        "and the external link is the mechanism used to capture your information."
    ),
    "how can i verify this safely": (
        "To verify safely: do not use any number, link, or contact information contained in the message itself. "
        "Instead, go directly to your bank's official website by typing the address yourself, "
        "log in and check your account status there, or call the number printed on the back of your debit/credit card. "
        "Official communications about account status will be visible within your account dashboard."
    ),
}

DEFAULT_DEMO_CHAT = (
    "Based on the analysis, this message contains indicators that suggest it may not be genuine. "
    "The safest approach is to verify any claims directly through the official organization's website "
    "or customer care, without using any links or numbers provided in the message itself."
)


def get_demo_analysis(message_lower: str) -> dict:
    """Return the most appropriate demo analysis for the given message."""
    if any(w in message_lower for w in ["bank", "account", "otp", "suspended", "verify"]):
        return DEMO_ANALYSES["banking"]
    if any(w in message_lower for w in ["job", "work-from-home", "registration fee", "selected", "congratulation"]):
        return DEMO_ANALYSES["job"]
    if any(w in message_lower for w in ["parcel", "delivery", "courier", "reschedule", "₹49"]):
        return DEMO_ANALYSES["delivery"]
    if any(w in message_lower for w in ["apk", "install", "download", "attachment", "document"]):
        return DEMO_ANALYSES["malware"]
    return DEMO_ANALYSES["benign"]


def get_demo_chat_response(question: str) -> str:
    """Return the best matching demo chat response for the given question."""
    q = question.lower().strip()
    for key, response in DEMO_CHAT_RESPONSES.items():
        if key in q:
            return response
    return DEFAULT_DEMO_CHAT
