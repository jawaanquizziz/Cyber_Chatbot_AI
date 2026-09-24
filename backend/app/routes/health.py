import os
from fastapi import APIRouter
from pydantic import BaseModel
from app.services import ollama_service

router = APIRouter()

class OllamaConfig(BaseModel):
    enabled: bool
    model: str
    url: str

@router.get("/health")
async def health_check():
    """Health check that also returns the mode for the TopNav status indicator."""
    gemini_key = os.getenv("GEMINI_API_KEY", "").strip()
    api_configured = bool(gemini_key)

    # Try to determine mode: live (Gemini key set), demo (Ollama up), else demo
    try:
        ollama_up = await ollama_service.check_status()
        ollama_available = ollama_up.get("available", False)
    except Exception:
        ollama_available = False

    if api_configured:
        mode = "live"
    elif ollama_available:
        mode = "live"   # Ollama is the live local LLM
    else:
        mode = "demo"   # Falls back to local NLP — still functional, not "offline"

    return {
        "status": "healthy",
        "mode": mode,
        "api_configured": api_configured,
        "ollama_available": ollama_available,
    }

@router.get("/ollama/status")
async def ollama_status():
    try:
        return await ollama_service.check_status()
    except Exception:
        return {"available": False, "model": None}

@router.get("/ollama/config", response_model=OllamaConfig)
async def get_config():
    return {
        "enabled": ollama_service.OLLAMA_ENABLED,
        "model": ollama_service.OLLAMA_MODEL,
        "url": ollama_service.OLLAMA_BASE_URL
    }

@router.post("/ollama/config")
async def update_config(config: OllamaConfig):
    ollama_service.OLLAMA_ENABLED = config.enabled
    ollama_service.OLLAMA_MODEL = config.model
    ollama_service.OLLAMA_BASE_URL = config.url.rstrip("/")
    return {"status": "success"}
