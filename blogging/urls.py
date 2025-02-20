from django.urls import path
from blogging.views import BlogListView, BlogDetailView, LatestPostsFeed

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("feed/", LatestPostsFeed()),
]
