from django.views.generic import DetailView, ListView, RedirectView

from .models import Author, Post, PostPreview


class BlogHomeView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "blog_home.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id,
        ).order_by("-created_at")
        return queryset


class BlogFeedView(ListView):
    context_object_name = "posts"
    model = Post
    content_type = "application/atom+xml"
    template_name = "feed.xml"

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id,
        ).order_by("-created_at")[:10]
        return queryset


class BlogPostView(DetailView):
    model = Post
    template_name = "blog_post.html"

    def get_object(self, queryset=None):
        post = self.model.objects.get(
            blog__site_id=self.request.site.id,
            short_code=self.kwargs.get("post_short_code"),
        )
        return post


class BlogPostPreviewView(DetailView):
    context_object_name = "post"
    model = PostPreview
    template_name = "blog_post.html"

    def get_object(self, queryset=None):
        post = self.model.objects.get(
            blog__site_id=self.request.site.id,
            short_code=self.kwargs.get("post_short_code"),
        )
        return post


class BlogCategoryView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "category_page.html"

    def get_context_data(self, **kwargs):
        context = super(BlogCategoryView, self).get_context_data(**kwargs)
        context["category_slug"] = self.kwargs["category_slug"]
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id,
            category__slug=self.kwargs["category_slug"],
        ).order_by("-created_at")
        return queryset


class BlogAuthorView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "author_page.html"

    def get_context_data(self, **kwargs):
        context = super(BlogAuthorView, self).get_context_data(**kwargs)
        context["author"] = Author.objects.get(
            slug=self.kwargs["author_slug"],
            blog__site_id=self.request.site.id,
        )
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id,
            author__slug=self.kwargs["author_slug"],
        ).order_by("-created_at")
        return queryset


class BlogAuthorFeedView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "author_feed.xml"

    def get_context_data(self, **kwargs):
        context = super(BlogAuthorFeedView, self).get_context_data(**kwargs)
        context["author"] = Author.objects.get(
            slug=self.kwargs["author_slug"],
            blog__site_id=self.request.site.id,
        )
        return context

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id,
            author__slug=self.kwargs["author_slug"],
        ).order_by("-created_at")[:10]
        return queryset


class PostsRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "/"
