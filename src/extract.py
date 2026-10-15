import time
import requests
from yaml import compose

BASE_URL = "http://127.0.0.1:8000"
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

def extract_customers() -> list[dict]:
    return extract_cycle(
        limit=2,
        offset=0,
        url=f"{BASE_URL}/customers"
    )


def extract_products() -> list[dict]:
    return extract_cycle(
        limit=2,
        offset=0,
        url=f"{BASE_URL}/products"
    )


def extract_orders() -> list[dict]:
    return extract_cycle(
        limit=2,
        offset=0,
        url=f"{BASE_URL}/orders"
    )


def extract_payments() -> list[dict]:
    return extract_cycle(
        limit=2,
        offset=0,
        url=f"{BASE_URL}/payments"
    )
def request_with_retry(url:str, params:dict, max_entries:int=3, backoff_factor:int = 2):
    for attempt in range(max_entries):
        try:
            response = requests.get(url, timeout=10, params=params)
            response.raise_for_status()
            return response
        except requests.Timeout as e:
            error = "Request timeout"
        except requests.ConnectionError as e:
            error = "Connection error"
        except requests.HTTPError as e:
            status_code = e.response.status_code
            if status_code not in RETRYABLE_STATUS_CODES:
                raise 
            error = f"HTTP {status_code}"
        
        if attempt == max_entries - 1:
            raise RuntimeError(f"Failed after {max_entries} attempts: {error}")
        wait_time = backoff_factor ** attempt
        print(f"{error}. Retrying in {wait_time}s...")
        time.sleep(wait_time)

def extract_cycle(
    url: str,
    limit: int = 2,
    offset: int = 0
) -> list[dict]:

    data = []

    while True:

        response = request_with_retry(
            url=url,
            params={
                "limit": limit,
                "offset": offset
            }
        )

        batch = response.json()

        if not batch:
            break

        data.extend(batch)

        offset += limit

    return data




