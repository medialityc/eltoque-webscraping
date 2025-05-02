from pydantic import BaseModel
from typing import Optional

class Currency(BaseModel):
    id: Optional[str] = None
    enabled: Optional[bool] = None
    code: Optional[str] = None
    name: Optional[str] = None
    flag_code: Optional[str] = None