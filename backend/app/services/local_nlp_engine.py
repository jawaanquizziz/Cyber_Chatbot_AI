"""
Local NLP Engine
Handles deterministic risk scoring, entity extraction, and indicators.
"""

def generate_local_analysis(message: str, preprocessed: dict) -> dict:
    risk_score = 0
    indicators = []
    entities = []
    
    # Process preprocessed signals
    if preprocessed.get("has_otp_reference"):
        risk_score += 40
        indicators.append({
            "name": "OTP Request",
            "explanation": "Message requests a One Time Password, often used in account takeovers."
        })
        entities.append({"type": "Requested Information", "value": "OTP"})
        
    if preprocessed.get("has_apk_or_executable"):
        risk_score += 60
        indicators.append({
            "name": "Suspicious Attachment",
            "explanation": "Message contains a reference to an APK or executable file."
        })
        entities.append({"type": "File Type", "value": "Executable/APK"})
        
    for url in preprocessed.get("urls", []):
        risk_score += 20
        entities.append({"type": "URL", "value": url})
    if preprocessed.get("urls"):
        indicators.append({
            "name": "Contains URL",
            "explanation": "Message directs the user to an external link."
        })
        
    urgency = preprocessed.get("urgency_signals", [])
    if urgency:
        risk_score += 15
        indicators.append({
            "name": "Urgency",
            "explanation": "Message uses urgent language to force immediate action."
        })
        for u in urgency:
            entities.append({"type": "Urgency", "value": u})
            
    credentials = preprocessed.get("credential_signals", [])
    if credentials:
        risk_score += 30
        indicators.append({
            "name": "Credential Request",
            "explanation": "Message requests passwords or personal information."
        })
        
    money = preprocessed.get("money", [])
    if money:
        risk_score += 10
        for m in money:
            entities.append({"type": "Money", "value": m})
            
    payment = preprocessed.get("payment_signals", [])
    if payment:
        risk_score += 15
        indicators.append({
            "name": "Payment Request",
            "explanation": "Message involves financial transactions or fees."
        })
        
    prize = preprocessed.get("prize_signals", [])
    if prize:
        risk_score += 25
        indicators.append({
            "name": "Prize/Offer",
            "explanation": "Message promises a prize or reward, typical of scams."
        })
        
    orgs = preprocessed.get("mentioned_organizations", [])
    for org in orgs:
        entities.append({"type": "Organization", "value": org})

    # Normalize risk score
    risk_score = min(risk_score, 100)
    
    risk_level = "LOW"
    if risk_score > 70:
        risk_level = "HIGH"
    elif risk_score > 30:
        risk_level = "MEDIUM"
        
    # Basic intent
    intent = "Informational"
    category = "No Significant Threat Detected"
    
    if risk_score > 30:
        if prize:
            intent = "Financial Fraud"
            category = "Job/Lottery Scam"
        elif credentials or preprocessed.get("has_otp_reference"):
            intent = "Credential Theft"
            category = "Potential Phishing"
        elif preprocessed.get("has_apk_or_executable"):
            intent = "Device Compromise"
            category = "Malware Distribution"
        elif payment:
            intent = "Payment Fraud"
            category = "Scam"
            
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "intent": intent,
        "category": category,
        "entities": entities,
        "indicators": indicators,
        "explanation": f"The message was analyzed locally. Risk score is {risk_score}/100. It contains {len(indicators)} risk indicators.",
        "recommended_actions": ["Exercise caution." if risk_score > 30 else "No immediate action required."],
    }

def get_local_chat_response(question: str) -> str:
    return "The message was flagged based on deterministic indicators such as links, urgency, or requests for sensitive information. Do not click suspicious links or share your OTP."
