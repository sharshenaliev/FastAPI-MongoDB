from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.config import db_settings
from src.documents import Test


@asynccontextmanager
async def lifespan(_app: FastAPI):
    client = AsyncIOMotorClient(db_settings.mongo_url)
    await init_beanie(database=client[db_settings.db_name], document_models=[Test])
    yield
