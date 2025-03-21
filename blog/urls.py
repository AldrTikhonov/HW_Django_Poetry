from django.urls import path
from blog.apps import BlogConfig

from blog.views import (
    BlogListViewAll,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogCreateView,
    BlogDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("list/", BlogListView.as_view(), name="blog_list"),
    path("list_all/", BlogListViewAll.as_view(), name="blog_list_all"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
]
