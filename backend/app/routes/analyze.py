from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.nlp.preprocessor import preprocess
from app.services import local_nlp_engine, ollama_service

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_message(request: AnalyzeRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    if len(message) > 5000:
        raise HTTPException(status_code=422, detail="Message exceeds maximum length of 5000 characters.")

    preprocessed = preprocess(message)
    
    # 1. Deterministic Local NLP Engine (Always available)
    local_result = local_nlp_engine.generate_local_analysis(message.lower(), preprocessed)
    
    # 2. Ollama Enrichment (Optional)
    is_ollama = False
    
    # The requirement says Ollama is optional and should fallback automatically
    try:
        ollama_status = await ollama_service.check_status()
        if ollama_status.get("available"):
            enrichment = await ollama_service.analyze_message(
                message=message,
                entities=local_result["entities"],
                indicators=local_result["indicators"],
                risk_score=local_result["risk_score"]
            )
            
            if enrichment:
                is_ollama = True
                local_result["intent"] = enrichment.get("intent", local_result["intent"])
                local_result["category"] = enrichment.get("category", local_result["category"])
                local_result["explanation"] = enrichment.get("explanation", local_result["explanation"])
                if enrichment.get("follow_up_answer"):
                    local_result["recommended_actions"].insert(0, enrichment.get("follow_up_answer"))
    except Exception as e:
        print(f"Ollama enrichment failed, falling back to local NLP: {e}")
        # Continue with local_result if Ollama fails

    return AnalyzeResponse(
        **local_result,
        is_demo=False,
        is_ollama=is_ollama,
        preprocessed=preprocessed,
    )
