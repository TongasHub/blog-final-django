"""Posts URLs."""

# Django
from django.urls import path, re_path

# Views
from posts import views

urlpatterns = [
    path(route="", view=views.PostsFeedView.as_view(), name="blog"),
    path(
        route="<str:filter_name>/",
        view=views.PostsFeedView.as_view(),
        name="filter",
    ),
    path(
        route="post/dateFilter/",
        view=views.PostsFeedView.as_view(),
        name="fecha",
    ),
    path(route="posts/<slug:url>/", view=views.PostDetailView.as_view(), name="detail"),
    path(route="posts/save_comment", view=views.save_comment, name="save_comment"),
]
