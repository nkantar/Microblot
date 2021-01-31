from django.urls import path

from microblot.core.views import dispatch

from .views import (
    BlogAuthorFeedView,
    BlogAuthorView,
    BlogCategoryView,
    BlogFeedView,
    BlogDraftView,
    BlogPostView,
    PostsRedirectView,
)


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
        "drafts/<post_short_code>/",
        dispatch,
        {
            "cms_class": BlogDraftView,
        },
        name="dispatch-draft",
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
    path(
        "authors/<author_slug>/",
        dispatch,
        {
            "cms_class": BlogAuthorView,
        },
        name="dispatch-author",
    ),
    path(
        "authors/<author_slug>/feed/",
        dispatch,
        {
            "cms_class": BlogAuthorFeedView,
        },
        name="dispatch-author-feed",
    ),
    path(
        "feed/",
        dispatch,
        {
            "cms_class": BlogFeedView,
        },
        name="dispatch-feed",
    ),
]
