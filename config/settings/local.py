from os import getenv

from .base import *  # noqa


DEBUG = True

FULL_DOMAIN = "microblot.local"
SHORT_DOMAIN = "blot.local"

FULL_DOMAINS = [FULL_DOMAIN, f"www.{FULL_DOMAIN}"]
SHORT_DOMAINS = [SHORT_DOMAIN, f"www.{SHORT_DOMAIN}"]

ALL_DOMAINS = [*FULL_DOMAINS, *SHORT_DOMAINS]

ALLOWED_HOSTS = [f".{FULL_DOMAIN}", f".{SHORT_DOMAIN}"]

SCHEME = "http"
PORT = ":8000"

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


RQ_QUEUES = {
    "default": {
        "HOST": "redis",
        "PORT": 6379,
        "DB": 0,
        "PASSWORD": getenv("REDIS_PASSWORD"),
    }
}

# Slack
SLACK_SIGNING_SECRET = getenv("SLACK_SIGNING_SECRET")
SLACK_VERIFICATION_TOKEN = getenv("SLACK_VERIFICATION_TOKEN")

# ngrok
NGROK_DOMAIN = getenv("NGROK_DOMAIN")
ALL_DOMAINS.append(NGROK_DOMAIN)
ALLOWED_HOSTS.append(NGROK_DOMAIN)
