import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import json
from core.config import ELTOQUE_URL, HEADERS
from utils.parser import extract_money_data


def create_session_with_retries(
        total_retries=5,
        backoff_factor=1,
        status_forcelist=(500, 502, 503, 504)
) -> requests.Session:
    session = requests.Session()
    retry_strategy = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def fetch_money_data():
    session = create_session_with_retries()
    response = session.get(ELTOQUE_URL, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Error accediendo a elTOQUE. Código HTTP: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find("script", id="__NEXT_DATA__")
    if not script:
        raise Exception("No se encontró el bloque __NEXT_DATA__")

    json_data = json.loads(script.string)
    return extract_money_data(json_data)
