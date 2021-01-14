from django.views.generic import DetailView, ListView

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
            short_code=self.request.GET.get("post_short_code", "1e76fd68"),
        )
        return post


# class BlogCategoryView(ListView)
# class BlogAuthorView(ListView)
