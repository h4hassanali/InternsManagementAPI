import beanie
import motor.motor_asyncio
from intern.models import Intern as intern
import os
from dotenv import load_dotenv


load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    await beanie.init_beanie(database = client.DATABASE_NAME, document_models = [intern])
    return client
