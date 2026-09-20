from fastapi import APIRouter
from app.services.gemini_service import is_configured

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ready",
        "mode": "live" if is_configured() else "demo",
        "api_configured": is_configured(),
    }
