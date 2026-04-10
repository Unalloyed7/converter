from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str
    password: str 

class UserDB(BaseModel):
    name: str
    hashpassword: str
    