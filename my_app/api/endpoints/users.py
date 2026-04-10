from fastapi import APIRouter, Depends, HTTPException

from my_app.api.core.database import get_db_connection
from my_app.api.core.security import authenticate_user, get_user_from_db, register_user
from my_app.api.models.users import User

app = APIRouter(prefix="/auth", tags=["Users"])


@app.post("/register", status_code=201)
async def register(user: User, db=Depends(get_db_connection)):
    if await get_user_from_db(user.name, db) is not None:
        raise HTTPException(status_code=409, detail="User already exists")
    await register_user(user, db)
    return {"message": "User registered successfully"}


@app.post("/login")
async def login(user: User, db=Depends(get_db_connection)):
    token = await authenticate_user(user, db)
    return {"access_token": token, "token_type": "bearer"}
