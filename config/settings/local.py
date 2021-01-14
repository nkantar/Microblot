from .base import *  # noqa


DEBUG = True

DOMAIN = "microblot.local"
ALLOWED_HOSTS = [f"{DOMAIN}"]

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
