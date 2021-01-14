from .base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = ["*.microblot.local"]

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
