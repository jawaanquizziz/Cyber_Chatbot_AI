from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services import gemini_service, demo_service

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(status_code=422, detail="Question cannot be empty.")

    use_demo = not gemini_service.is_configured()

    if use_demo:
        answer = demo_service.get_demo_chat_response(question)
        return ChatResponse(answer=answer, is_demo=True)

    try:
        answer = await gemini_service.chat_response(question, request.analysis_context)
        return ChatResponse(answer=answer, is_demo=False)
    except Exception:
        # Fallback to demo chat on any API failure
        answer = demo_service.get_demo_chat_response(question)
        return ChatResponse(answer=answer, is_demo=True)
