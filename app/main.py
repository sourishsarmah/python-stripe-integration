from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routers.api import router
from app.core.config import ALLOWED_HOSTS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
