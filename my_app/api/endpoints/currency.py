from fastapi import *
from my_app.api.core.security import *
from my_app.api.utils.external_api import *
from my_app.api.models.currency import *

app = APIRouter(prefix = "/currency", tags=["Currency"])

@app.get("/list")
def get(user = Depends(get_user_from_token)):
    return get_currency_list()

@app.get("/exchange")
def exchange(source: str, target: str, user=Depends(get_user_from_token)):
    return get_live_rate(source, target)


@app.post("/convert")
def convertcoin(req: Exccur, user = Depends(get_user_from_token)):
    return convert(req.from_currency, req.to_currency, req.amount)