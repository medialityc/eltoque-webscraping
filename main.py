from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="🏴‍☠️ elTOQUE Pirata API 🏴‍☠️",
    description="### Feliz cumpleaños elToque, te pirateamos la API.",
    version="1.0.0"
)

# noinspection PyTypeChecker
# pyright: reportArgumentType=false
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
