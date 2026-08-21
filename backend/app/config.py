import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    Central application configuration.
    """

    BASE_URL = os.getenv("BASE_URL", "").rstrip("/")
    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()