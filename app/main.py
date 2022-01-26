import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.api.routers.api import router
from app.core.config import ALLOWED_HOSTS

app = FastAPI()

print(os.getcwd())
app.mount(
    "/ui",
    StaticFiles(
        directory="/media/sourish/SSD/Codes/assignments/python-stripe-integration/client"
    ),
    name="static",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
