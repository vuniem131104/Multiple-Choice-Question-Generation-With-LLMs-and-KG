import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router
from auth.database import Database
from auth.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.settings = get_settings()
    app.state.db = Database(app.state.settings)
    await app.state.db.connect()
    
    yield
    
    # Shutdown
    await app.state.db.disconnect()


app = FastAPI(
    title="Authentication Service",
    description="JWT-based authentication for educational platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "auth"}


# Dependency injection for database and settings
from fastapi import Request


async def get_db(request: Request) -> Database:
    return request.app.state.db


async def get_settings_dep(request: Request):
    return request.app.state.settings


# Override dependencies
from auth.routes import router as auth_router
auth_router.dependencies = [
    *auth_router.dependencies,
]

app.dependency_overrides[Database] = get_db
app.dependency_overrides[get_settings] = get_settings_dep


def main():
    uvicorn.run(
        "auth:app",
        host="0.0.0.0",
        port=3001,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()
