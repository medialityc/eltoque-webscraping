from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

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

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/healthcheck", response_class=HTMLResponse, tags=["Healthcheck"])
async def healthcheck_page(request: Request):
    return templates.TemplateResponse("healthcheck.html", {"request": request})

app.include_router(router)
