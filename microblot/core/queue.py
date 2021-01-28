from datetime import timedelta

import django_rq

from django.conf import settings


def enqueue_in(ttl_in, func, *args, **kwargs):
    if settings.RQ_ENABLED:
        queue = django_rq.get_queue("default")
        queue.enqueue_in(ttl_in, func, *args, **kwargs)
    else:
        func(*args, **kwargs)


def enqueue(func, *args, **kwargs):
    enqueue_in(timedelta(seconds=0), func, *args, **kwargs)
