from __future__ import annotations

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from logger import get_logger
from logger import setup_logging
from lite_llm import LiteLLMService
from storage.minio import MinioService

from generation.api.routers.quiz_generation import quiz_router
from generation.api.routers.upload import upload_router
from generation.shared.utils import get_settings


setup_logging(json_logs=False, log_level='INFO')
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = get_settings()
    app.state.litellm_service = LiteLLMService(
        litellm_setting=app.state.settings.litellm
    )
    app.state.minio_service = MinioService(
        settings=app.state.settings.minio
    )
    
    yield 


app = FastAPI(
    title='Multiple-Choie Questions Generation Service',
    description='Service for generating Multiple-Choie Questions',
    version='0.1.0',
    lifespan=lifespan,
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz_router)
app.include_router(upload_router)

def main():
    uvicorn.run(
        "generation:app",
        host='0.0.0.0',
        port=3005,
        log_level='info',
        reload=True,
    )
