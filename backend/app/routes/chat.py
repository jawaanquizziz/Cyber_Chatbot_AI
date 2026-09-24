from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services import local_nlp_engine, ollama_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    question = request.question.strip()

    if not question:
        raise HTTPException(status_code=422, detail="Question cannot be empty.")

    is_ollama = False
    
    try:
        ollama_status = await ollama_service.check_status()
        if ollama_status.get("available"):
            answer = await ollama_service.chat_response(question, request.analysis_context)
            if answer:
                is_ollama = True
                return ChatResponse(answer=answer, is_demo=False, is_ollama=True)
    except Exception as e:
        print(f"Ollama chat failed, falling back to local NLP: {e}")
        
    # Fallback to local response generator
    answer = local_nlp_engine.get_local_chat_response(question)
    return ChatResponse(answer=answer, is_demo=False, is_ollama=False)
