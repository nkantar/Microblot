from .base import *  # noqa


DEBUG = False

FULL_DOMAIN = "microblot.dev"
SHORT_DOMAIN = "blot.dev"
ALLOWED_HOSTS = [f".{FULL_DOMAIN}", f".{SHORT_DOMAIN}"]
