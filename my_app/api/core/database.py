from fastapi import Request


async def get_db_connection(request: Request):
    return request.app.state.db


async def create_table(db):
    await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
