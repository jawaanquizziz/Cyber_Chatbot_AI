import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, analyze, chat

app = FastAPI(
    title="CyberGuard API",
    description="Message security analysis backend",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url=None,
)

cors_origins_env = os.getenv("ALLOWED_ORIGINS", "*")
allowed_origins = [o.strip() for o in cors_origins_env.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins != ["*"] else ["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/api")
@app.get("/api/")
@app.get("/api/index")
@app.get("/api/index.py")
async def root():
    return {"status": "ok", "message": "CyberGuard API is operational"}

# Route handlers mounted at /api
app.include_router(health.router, prefix="/api")
app.include_router(analyze.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

# Fallback routes without /api prefix for serverless function rewrites
app.include_router(health.router)
app.include_router(analyze.router)
app.include_router(chat.router)
