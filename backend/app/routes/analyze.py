from fastapi import APIRouter, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.nlp.preprocessor import preprocess
from app.services import gemini_service, demo_service

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_message(request: AnalyzeRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    if len(message) > 5000:
        raise HTTPException(status_code=422, detail="Message exceeds maximum length of 5000 characters.")

    preprocessed = preprocess(message)

    # Use demo mode if explicitly requested or API is not configured
    use_demo = request.demo_mode or not gemini_service.is_configured()

    if use_demo:
        result = demo_service.get_demo_analysis(message.lower())
        return AnalyzeResponse(
            **result,
            is_demo=True,
            preprocessed=preprocessed,
        )

    try:
        result = await gemini_service.analyze_message(message, preprocessed)
        return AnalyzeResponse(
            **result,
            is_demo=False,
            preprocessed=preprocessed,
        )
    except ValueError as e:
        raise HTTPException(status_code=502, detail=f"Analysis failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=503, detail="Analysis service unavailable. Try using demo mode.")
