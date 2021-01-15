from django.urls import path

from microblot.core.views import dispatch

from .views import ShortenerPostRedirectView


# NOTE: See microblot.config.urls for some shared routes.


urlpatterns = [
    path(
        "<post_short_code>",
        dispatch,
        {
            "short_class": ShortenerPostRedirectView,
        },
        name="dispatch-short",
    ),
]
