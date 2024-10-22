from contextlib import asynccontextmanager
from fastapi import FastAPI
from intern.routes import intern_router
from database.client import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await init_db()
    try:
        yield
    finally:
        client.close()
app = FastAPI(lifespan=lifespan)
app.include_router(intern_router, prefix="/intern")
