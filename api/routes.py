from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse

from services.scraper import fetch_money_data
from models.response.api_response import ApiResponse

router = APIRouter()

@router.get("/api/piratear-eltoque", summary="Piratear a elToque", response_model=ApiResponse, tags=["😈😈😈"])
def get_money_data():
    """
    Devuelve los datos de las tasas de cambio, al igual que las monedas procesadas
    por elToque.
    **IMPORTANTE**: Esa gente usa la _mediana_ (`median`) para mostrar las tasas.
    """
    try:
        return fetch_money_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")