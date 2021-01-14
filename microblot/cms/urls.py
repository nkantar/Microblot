from django.urls import path

from .views import (
    # BlogAuthorView,
    # BlogCategoryView,
    BlogHomeView,
    BlogPostView,
)


urlpatterns = [
    path("", BlogHomeView.as_view(), name="blog-home"),
    path("posts/<post_short_code>", BlogPostView.as_view(), name="blog-post"),
    # path("<author_slug>", BlogAuthorView.as_view()),
    # path("<category_slug>", BlogCategoryView.as_view()),
]
