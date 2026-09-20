import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

# 1. API Route Handlers
app.include_router(health.router, prefix="/api")
app.include_router(analyze.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

# Fallback routes without /api prefix
app.include_router(health.router)
app.include_router(analyze.router)
app.include_router(chat.router)

@app.get("/api")
@app.get("/api/")
@app.get("/api/index")
@app.get("/api/index.py")
async def api_root():
    return {"status": "ok", "message": "CyberGuard API is operational"}

@app.get("/api/debug-paths")
async def debug_paths():
    cur = Path(__file__).resolve()
    return {
        "file": str(cur),
        "cwd": os.getcwd(),
        "cwd_files": [p.name for p in Path(".").iterdir()],
        "task_files": [p.name for p in cur.parent.parent.parent.iterdir()] if cur.parent.parent.parent.exists() else [],
    }

# 2. Static Frontend & SPA Fallback
dist_dir = None
for candidate in [
    Path(__file__).resolve().parent.parent.parent / "dist",
    Path(__file__).resolve().parent.parent / "dist",
    Path("dist").resolve(),
    Path("frontend/dist").resolve(),
]:
    if candidate.exists() and (candidate / "index.html").exists():
        dist_dir = candidate
        break

if dist_dir:
    assets_dir = dist_dir / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/")
    async def serve_root():
        return FileResponse(dist_dir / "index.html")

    @app.get("/favicon.svg")
    async def serve_favicon():
        fav = dist_dir / "favicon.svg"
        if fav.exists():
            return FileResponse(fav)
        return FileResponse(dist_dir / "index.html")

    @app.get("/icons.svg")
    async def serve_icons():
        ic = dist_dir / "icons.svg"
        if ic.exists():
            return FileResponse(ic)
        return FileResponse(dist_dir / "index.html")

    @app.get("/{full_path:path}")
    async def serve_spa_routes(full_path: str):
        if full_path.startswith("api/") or full_path == "api":
            raise HTTPException(status_code=404, detail="API route not found")
        target = dist_dir / full_path
        if target.is_file():
            return FileResponse(target)
        return FileResponse(dist_dir / "index.html")
else:
    @app.get("/")
    async def serve_no_dist():
        return {"status": "ok", "message": "CyberGuard API is operational"}
