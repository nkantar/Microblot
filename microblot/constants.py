from os import getenv
from pathlib import Path


DEBUG = bool(getenv("DEBUG", False))

ENVIRONMENT = getenv("ENVIRONMENT", "development")

CURRENT_DIR = Path.cwd()

_DATABASES = {"development": f"sqlite:///{CURRENT_DIR / 'dev_db.db'}"}
DATABASE = _DATABASES[ENVIRONMENT]
