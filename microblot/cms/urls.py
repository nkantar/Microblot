from django.urls import path

from microblot.core.views import dispatch

from .views import BlogPostView, BlogCategoryView, PostsRedirectView


# NOTE: See config/urls.py for some shared routes.


urlpatterns = [
    path(
        "posts/<post_short_code>/",
        dispatch,
        {
            "cms_class": BlogPostView,
        },
        name="dispatch-post",
    ),
    path(
        "posts/",
        dispatch,
        {
            "cms_class": PostsRedirectView,
        },
        name="dispatch-posts",
    ),
    path(
        "categories/<category_slug>/",
        dispatch,
        {
            "cms_class": BlogCategoryView,
        },
        name="dispatch-category",
    ),
]
