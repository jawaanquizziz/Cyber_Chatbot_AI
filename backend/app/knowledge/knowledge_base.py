from typing import Optional, List
"""
Cybersecurity knowledge base.
Used to enrich AI prompts and power the Security Guide page.
"""

KNOWLEDGE_BASE: dict = {
    "phishing": {
        "title": "Phishing",
        "definition": (
            "Phishing is a deceptive attempt to steal sensitive information such as "
            "account credentials, OTPs, or financial details by impersonating a trusted "
            "entity through email, SMS, or messaging platforms."
        ),
        "common_indicators": [
            "Urgent language pressuring immediate action",
            "Requests for OTPs, passwords, or account details",
            "Links to lookalike websites mimicking legitimate organizations",
            "Threats of account suspension or legal action",
            "Unexpected verification requests",
        ],
        "safe_response": (
            "Do not click any links. Do not provide any personal information. "
            "Verify the request by contacting the organization directly through "
            "their official website or customer care number."
        ),
        "prevention": (
            "Enable two-factor authentication. Bookmark official websites. "
            "Always verify sender domains. Report suspicious messages to your bank or IT team."
        ),
    },
    "smishing": {
        "title": "Smishing (SMS Phishing)",
        "definition": (
            "Smishing is phishing conducted via SMS or messaging apps. "
            "Attackers send fake text messages impersonating banks, delivery services, "
            "or government agencies to trick recipients into clicking links or sharing credentials."
        ),
        "common_indicators": [
            "Unsolicited SMS from an unknown number",
            "Link to a shortened or suspicious URL",
            "Requests to call a specific number",
            "Claimed prize or lottery win",
            "Fake delivery notification with payment request",
        ],
        "safe_response": (
            "Do not click links in unsolicited SMS messages. "
            "Go directly to the official website or app of the organization instead."
        ),
        "prevention": (
            "Register for Do Not Disturb (DND) services. "
            "Use SMS filtering features on your phone. "
            "Never trust a sender's name alone — verify through official channels."
        ),
    },
    "vishing": {
        "title": "Vishing (Voice Phishing)",
        "definition": (
            "Vishing uses phone calls to manipulate victims into revealing sensitive "
            "information. Attackers may impersonate bank representatives, government "
            "officials, or technical support agents."
        ),
        "common_indicators": [
            "Unsolicited call claiming to be from your bank or a government agency",
            "Request for OTP, CVV, or account credentials over the phone",
            "Threats of immediate account suspension or legal action",
            "Caller insists you must act right now",
            "Request to install remote access software",
        ],
        "safe_response": (
            "Hang up immediately. Call back using the official number on the organization's website. "
            "Never share OTPs or passwords over the phone — no legitimate organization asks for them."
        ),
        "prevention": (
            "Banks and government agencies never ask for OTPs or PINs over the phone. "
            "Be suspicious of unsolicited calls, especially those creating urgency."
        ),
    },
    "credential_theft": {
        "title": "Credential Theft",
        "definition": (
            "Credential theft refers to attempts to steal usernames, passwords, PINs, OTPs, "
            "or other authentication information to gain unauthorized access to accounts."
        ),
        "common_indicators": [
            "Request to enter OTP, password, or PIN on a website or form",
            "Fake login pages that mimic legitimate services",
            "Requests sent urgently before verification is possible",
            "Unexpected account verification messages",
        ],
        "safe_response": (
            "Never enter credentials on a page you reached through a link in a message. "
            "Always navigate directly to the official website."
        ),
        "prevention": (
            "Use a password manager. Enable two-factor authentication. "
            "Check the URL carefully before logging in. "
            "OTPs should only be entered on the official app or website that generated them."
        ),
    },
    "social_engineering": {
        "title": "Social Engineering",
        "definition": (
            "Social engineering is the psychological manipulation of people into taking "
            "actions or revealing information. It exploits trust, authority, urgency, and fear "
            "rather than technical vulnerabilities."
        ),
        "common_indicators": [
            "Creates a sense of urgency or fear",
            "Appeals to authority (police, bank, government)",
            "Requests secrecy ('do not tell anyone about this')",
            "Offers that seem too good to be true",
            "Builds trust before making a request",
        ],
        "safe_response": (
            "Slow down. Verify independently before acting. "
            "Talk to someone you trust before responding to unusual requests."
        ),
        "prevention": (
            "Be sceptical of unsolicited contacts. Verify identities independently. "
            "Legitimate organizations do not pressure you to act immediately."
        ),
    },
    "job_scam": {
        "title": "Job Scams",
        "definition": (
            "Job scams offer fake work-from-home or freelance positions and ask victims "
            "to pay registration fees, processing fees, or training costs before receiving "
            "any work or payment."
        ),
        "common_indicators": [
            "Unsolicited job offer via WhatsApp, SMS, or Telegram",
            "Request to pay a fee before starting work",
            "Unusually high pay for simple tasks",
            "No verifiable company details or interview process",
            "Tasks involve liking videos, completing surveys, or rating products",
        ],
        "safe_response": (
            "Legitimate employers do not require payment from job applicants. "
            "Do not pay any registration or processing fee. Report to cybercrime.gov.in."
        ),
        "prevention": (
            "Only apply to jobs through verified platforms. "
            "Research the company independently. "
            "Never pay money to get a job."
        ),
    },
    "delivery_scam": {
        "title": "Delivery Scams",
        "definition": (
            "Delivery scams impersonate courier services and send fake notifications about "
            "undelivered parcels, asking recipients to pay small fees to reschedule delivery "
            "or update their address."
        ),
        "common_indicators": [
            "Unexpected delivery failure notification",
            "Request to pay a small fee (₹20–₹99) to reschedule",
            "Link to a website that does not match the official courier domain",
            "No order reference number or tracking ID provided",
        ],
        "safe_response": (
            "Go directly to the official courier website and use your tracking number. "
            "Do not click links in unsolicited delivery SMS messages."
        ),
        "prevention": (
            "Legitimate couriers do not request payment via SMS links. "
            "Always verify through the official courier app or website."
        ),
    },
    "banking_scam": {
        "title": "Banking Scams",
        "definition": (
            "Banking scams impersonate banks or financial institutions to steal account "
            "credentials, card details, or OTPs. They often threaten account suspension "
            "to create urgency."
        ),
        "common_indicators": [
            "Claim that your account will be suspended or blocked",
            "Request to verify your account through a link",
            "Asks for OTP, CVV, or net banking credentials",
            "Sender number does not match official bank numbers",
            "Link domain does not match the bank's official website",
        ],
        "safe_response": (
            "Call the bank's official customer care number directly. "
            "Do not use any number or link provided in the suspicious message."
        ),
        "prevention": (
            "Banks never ask for OTPs or passwords via SMS or call. "
            "Regularly check your bank's official communication guidelines."
        ),
    },
    "investment_scam": {
        "title": "Investment Scams",
        "definition": (
            "Investment scams promise high returns with low risk to lure victims into "
            "transferring money to fraudulent investment schemes, crypto platforms, or trading apps."
        ),
        "common_indicators": [
            "Guaranteed returns or risk-free investment claims",
            "Pressure to invest quickly before an offer expires",
            "Requests to install an unknown trading app",
            "Referral-based earning model",
            "Payment required to withdraw earnings",
        ],
        "safe_response": (
            "Do not invest based on unsolicited messages. "
            "Verify investment platforms through SEBI's registered intermediaries list."
        ),
        "prevention": (
            "If returns sound too good, they are not real. "
            "Only use SEBI-registered platforms. "
            "Report suspicious schemes at cybercrime.gov.in."
        ),
    },
    "malware": {
        "title": "Malware & Malicious Files",
        "definition": (
            "Malware attacks trick users into downloading and installing malicious software "
            "disguised as documents, media files, or applications. Once installed, the software "
            "can steal data, monitor activity, or take control of the device."
        ),
        "common_indicators": [
            "Request to download an APK file outside the Play Store or App Store",
            "Link to download a document from an unknown source",
            "Message claiming a file has been shared with you",
            "Request to install a remote access or screen-sharing app",
        ],
        "safe_response": (
            "Do not download or install files from unknown sources. "
            "Only install applications from the official Google Play Store or Apple App Store."
        ),
        "prevention": (
            "Disable 'Install from unknown sources' on Android. "
            "Keep your device OS and apps updated. "
            "Use device security settings to scan apps before installation."
        ),
    },
    "impersonation": {
        "title": "Impersonation",
        "definition": (
            "Impersonation attacks involve an attacker pretending to be a trusted person "
            "or organization — a bank, employer, government agency, or even a family member — "
            "to manipulate the victim into complying with a fraudulent request."
        ),
        "common_indicators": [
            "Message claims to be from a known brand or authority",
            "Creates urgency using the authority's name",
            "Requests are inconsistent with how the real organization communicates",
            "Sender address or number does not match official records",
        ],
        "safe_response": (
            "Verify the identity of the sender through official channels independently. "
            "Do not use contact information provided within the suspicious message."
        ),
        "prevention": (
            "Familiarise yourself with how your bank and key services communicate. "
            "When in doubt, hang up and call back using the official number."
        ),
    },
}


def get_category_info(category_key: str) -> Optional[dict]:
    return KNOWLEDGE_BASE.get(category_key.lower().replace(" ", "_"))


def get_all_categories() -> List[dict]:
    return [{"key": k, **v} for k, v in KNOWLEDGE_BASE.items()]
