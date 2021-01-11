from os import getenv
from pathlib import Path


DEBUG = bool(getenv("DEBUG", False))

ENVIRONMENT = getenv("ENVIRONMENT", "development")

POSTGRES_HOST = getenv("POSTGRES_HOST", "db")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
DATABASE = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)
