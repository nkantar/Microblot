from django.conf import settings
from django.http import Http404


def dispatch(request, main_class=None, cms_class=None, short_class=None, **kwargs):
    """
    Delegate to the correct class based on the current site.

    This helper view allows the user to delegate the request to the correct class based
    on the current site. This allows for different apps with their own needs to "share"
    URLs when appropriate.

    Each of the "_class" params corresponds to a view class for the desired app.
    """
    classes = {
        settings.FULL_DOMAIN: main_class,
        f"www.{settings.FULL_DOMAIN}": main_class,
        settings.SHORT_DOMAIN: short_class,
        f"www.{settings.SHORT_DOMAIN}": short_class,
    }
    target_class = classes.get(request.site.domain, cms_class)

    if target_class is None:
        raise Http404()

    return target_class.as_view()(request, **kwargs)
