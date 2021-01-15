from .base import *  # noqa


DEBUG = False

FULL_DOMAIN = "microblot.io"
SHORT_DOMAIN = "blot.click"
ALLOWED_HOSTS = [f".{FULL_DOMAIN}", f".{SHORT_DOMAIN}"]
