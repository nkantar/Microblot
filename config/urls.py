"""microblot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings

from microblot.cms.views import BlogHomeView, BlogPostView
from microblot.core.views import dispatch
from microblot.main.views import MainHomeView
from microblot.shortener.views import ShortenerHomeRedirectView, ShortenerRedirectView

urlpatterns = [
    path(
        "",
        dispatch,
        {
            "main_class": MainHomeView,
            "cms_class": BlogHomeView,
            "short_class": ShortenerHomeRedirectView,
        },
        name="dispatch-home",
    ),
    path(
        "posts/<post_short_code>",
        dispatch,
        {
            "main_class": None,
            "cms_class": BlogPostView,
            "short_class": None,
        },
        name="dispatch-post",
    ),
    path(
        "<post_short_code>",
        dispatch,
        {
            "main_class": None,
            "cms_class": None,
            "short_class": ShortenerRedirectView,
        },
        name="dispatch-short",
    ),
]


if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
