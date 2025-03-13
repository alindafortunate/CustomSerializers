from django.urls import path
from .views import BlogPostView, BlogPostViewWithComments, post_detail

urlpatterns = [
    path("posts/", BlogPostView.as_view(), name="blog-posts"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
    path(
        "posts-and-comments/",
        BlogPostViewWithComments.as_view(),
        name="blog-post-comments",
    ),
]
