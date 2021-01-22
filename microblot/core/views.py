from switchlang import switch

from django.conf import settings
from django.http import Http404
from django.views.generic import View


class PageNotFoundView(View):
    """
    Fallback view for the dispatch helper below.

    All this view does is return a 404, and its sole purpose is decluttering the
    dispatch helper view defined below.

    By using it as the default value for parameters to dispatch, dispatch doesn't have
    to explicitly account for omitted classes, and can just call the as_view method.
    """

    def dispatch(self, request, *args, **kwargs):
        raise Http404()


def dispatch(
    request,
    main_class=PageNotFoundView,
    cms_class=PageNotFoundView,
    short_class=PageNotFoundView,
    **kwargs
):
    """
    Delegate to the correct class based on the current site.

    This helper view allows the user to delegate the request to the correct class based
    on the current site. This allows for different apps with their own needs to "share"
    URLs when appropriate.

    Each of the "_class" params corresponds to a view class for the desired app.
    """
    with switch(request.site.domain) as app:
        app.case(settings.FULL_DOMAINS, lambda: main_class)
        app.case(settings.SHORT_DOMAINS, lambda: short_class)
        app.default(lambda: cms_class)

    return app.result.as_view()(request, **kwargs)
