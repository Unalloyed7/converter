from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from my_app.api.core.config import DATABASE_URL
from my_app.api.core.database import create_table
from my_app.api.endpoints.users import app as users_router
from my_app.api.endpoints.currency import app as currency_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await asyncpg.create_pool(DATABASE_URL)
    await create_table(app.state.db)
    yield
    await app.state.db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(users_router)
app.include_router(currency_router)
