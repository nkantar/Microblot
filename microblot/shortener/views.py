from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView

from microblot.cms.models import Post


class ShortenerHomeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = f"{settings.SCHEME}://www.{settings.FULL_DOMAIN}{settings.PORT}"
        return url


class ShortenerPostRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, short_code=kwargs.get("post_short_code"))
        url = redirect(post).url
        return url
