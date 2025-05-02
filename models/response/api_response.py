from typing import List, Optional


from pydantic import BaseModel

from models.response.currency import Currency
from models.response.exchange_rate import ExchangeRate

class ApiResponse(BaseModel):
    currencies: List[Currency]
    exchange_rates: List[ExchangeRate]
    datetime: Optional[str] = None