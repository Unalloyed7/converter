import requests
from fastapi import HTTPException
from my_app.api.core.config import CURRENCY_API_KEY

def get_currency_list():
    try:
        response = requests.get(
            "https://api.apilayer.com/currency_data/list",
            headers={"apikey": CURRENCY_API_KEY},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as exc:
        response = exc.response
        if response is not None and response.status_code in {400, 404, 422}:
            raise HTTPException(status_code=400, detail="Invalid currency code or request")
        raise HTTPException(status_code=502, detail="Currency service unavailable")
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Currency service unavailable")


def get_live_rate(source: str, target: str):
    try:
        response = requests.get(
            "https://api.apilayer.com/currency_data/live",
            headers={"apikey": CURRENCY_API_KEY},
            params={"source": source, "currencies": target},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as exc:
        response = exc.response
        if response is not None and response.status_code in {400, 404, 422}:
            raise HTTPException(status_code=400, detail="Invalid currency code or request")
        raise HTTPException(status_code=502, detail="Currency service unavailable")
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Currency service unavailable")


def convert(from_currency: str, to_currency: str, amount: float):
    try:
        response = requests.get(
            "https://api.apilayer.com/currency_data/convert",
            headers={"apikey": CURRENCY_API_KEY},
            params={"from": from_currency, "to": to_currency, "amount": amount},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as exc:
        response = exc.response
        if response is not None and response.status_code in {400, 404, 422}:
            raise HTTPException(status_code=400, detail="Invalid currency code or request")
        raise HTTPException(status_code=502, detail="Currency service unavailable")
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Currency service unavailable")
