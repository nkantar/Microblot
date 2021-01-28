import django_rq

from django.conf import settings


def enqueue(func, *args, **kwargs):
    if settings.RQ_ENABLED:
        django_rq.enqueue(func, *args, **kwargs)
    else:
        func(*args, **kwargs)
