from switchlang import switch

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

    with switch(request.site.domain) as domain:
        domain.case(settings.FULL_DOMAINS, lambda: main_class)
        domain.case(settings.SHORT_DOMAINS, lambda: short_class)
        domain.default(lambda: cms_class)

    if domain.result is None:
        raise Http404()

    return domain.result.as_view()(request, **kwargs)
