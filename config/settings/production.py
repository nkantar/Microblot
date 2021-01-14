from .base import *  # noqa


DEBUG = False

MAIN_DOMAIN = "microblot.io"
SHORT_DOMAIN = "blot.click"
ALLOWED_HOSTS = [f".{MAIN_DOMAIN}", f".{SHORT_DOMAIN}"]
