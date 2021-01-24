from django.views.generic import DetailView, ListView, RedirectView

from .models import Post


class BlogHomeView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "blog_home.html"

    def get_queryset(self):
        queryset = self.model.objects.filter(
            blog__site_id=self.request.site.id
        ).order_by("-created_at")
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


# class BlogAuthorView(ListView)


class PostsRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "/"
