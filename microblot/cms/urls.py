from django.urls import path

from .views import (
    # BlogAuthorView,
    # BlogCategoryView,
    BlogHomeView,
    BlogPostView,
)


urlpatterns = [
    path("", BlogHomeView.as_view()),
    path("<post_short_code>", BlogPostView.as_view()),
    # path("<author_slug>", BlogAuthorView.as_view()),
    # path("<category_slug>", BlogCategoryView.as_view()),
]
