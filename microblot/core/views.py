from django.conf import settings
from django.http import Http404


def dispatch(request, main_class=None, cms_class=None, short_class=None, **kwargs):
    classes = {
        settings.FULL_DOMAIN: main_class,
        f"www.{settings.FULL_DOMAIN}": main_class,
        settings.SHORT_DOMAIN: short_class,
        f"www.{settings.SHORT_DOMAIN}": short_class,
    }
    class_ = classes.get(request.site.domain, cms_class)

    if class_ is None:
        raise Http404()

    return class_.as_view()(request, **kwargs)
