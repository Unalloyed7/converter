from pydantic import BaseModel, Field, EmailStr


class Livecur(BaseModel):
    source: str
    target: str

class Exccur(BaseModel):
    from_currency : str
    to_currency : str
    amount: float
    