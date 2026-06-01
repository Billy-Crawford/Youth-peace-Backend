# resources_app/urls.py

from django.urls import path

from .views import (
    ResourceListCreateView,
    ResourceDetailView,
    ToggleFavoriteView,
    FavoriteListView,
)

urlpatterns = [

    path(
        "",
        ResourceListCreateView.as_view()
    ),

    path(
        "<uuid:pk>/",
        ResourceDetailView.as_view()
    ),

    path(
        "<uuid:resource_id>/favorite/",
        ToggleFavoriteView.as_view()
    ),

    path(
        "favorites/",
        FavoriteListView.as_view()
    ),
]


