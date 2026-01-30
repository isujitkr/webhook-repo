from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not DB_NAME:
    raise ValueError("DB_NAME is not set in .env")

try:
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")
    print("MongoDB connected successfully")

except Exception as e:
    print("MongoDB connection failed")
    print(e)
    raise e

db = client[DB_NAME]
events_collection = db.events
