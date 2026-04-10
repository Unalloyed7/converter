import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt

from my_app.api.core.database import get_db_connection
from my_app.api.models.users import User, UserDB
from my_app.api.core.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_user_from_db(name: str, db=Depends(get_db_connection)):
    res = await db.fetchrow(
        """
        SELECT name, password
        FROM users
        WHERE name = $1
        """,
        name
    )
    return res


async def register_user(user: User, db=Depends(get_db_connection)):
    res = UserDB(name=user.name, hashpassword=bcrypt.hash(user.password))
    await db.execute(
        """
        INSERT INTO users(name, password)
        VALUES ($1, $2)
        """,
        res.name,
        res.hashpassword
    )


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def authenticate_user(user: User, db=Depends(get_db_connection)):
    userdb = await get_user_from_db(user.name, db)
    if userdb is None or not bcrypt.verify(user.password, userdb["password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return create_jwt_token({"sub": userdb["name"]})


async def get_user_from_token(
    token: str = Depends(oauth2_scheme), db=Depends(get_db_connection)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = await get_user_from_db(username, db)
        if user is None:
            raise credentials_exception
        return user
    except jwt.InvalidTokenError:
        raise credentials_exception
