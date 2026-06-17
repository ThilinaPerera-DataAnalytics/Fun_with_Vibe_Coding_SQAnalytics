import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file")

# Create database engine
engine = create_engine(DATABASE_URL)

print("Database connection configuration loaded.")