from .base import *  # noqa


DEBUG = False

MAIN_DOMAIN = "microblot.dev"
SHORT_DOMAIN = "blot.dev"
ALLOWED_HOSTS = [f".{MAIN_DOMAIN}", f".{SHORT_DOMAIN}"]
