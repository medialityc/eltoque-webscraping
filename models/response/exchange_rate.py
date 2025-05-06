from typing import Optional, List

from pydantic import BaseModel


class ExchangeRate(BaseModel):
    currency_code: Optional[str] = None
    avg: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    median: Optional[float] = None
    standard_deviation: Optional[float] = None
    count_values: Optional[int] = None
    count_messages: Optional[int] = None
    p_avg: Optional[float] = None
    avg_diff: Optional[float] = None
    p_min: Optional[float] = None
    min_diff: Optional[float] = None
    p_max: Optional[float] = None
    max_diff: Optional[float] = None
    p_median: Optional[float] = None
    median_diff: Optional[float] = None
    p_count_values: Optional[float] = None
    p_count_messages: Optional[float] = None
    unstable: Optional[bool] = None
    tendency: Optional[str] = None
