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


# class BlogCategoryView(ListView)
# class BlogAuthorView(ListView)


class PostsRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return "/"
