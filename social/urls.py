# social/urls.py

from django.urls import path

from .views import (
    PostListCreateView,
    PostDetailView, CommentListCreateView, ToggleLikeView, InitiativeListCreateView, InitiativeDetailView,
    ForumTopicListCreateView, ForumTopicDetailView, ForumReplyListCreateView,
)

urlpatterns = [
    path(
        "",
        PostListCreateView.as_view(),
        name="post-list-create",
    ),

    path(
        "<uuid:pk>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),

    path(
        "<uuid:post_id>/comments/",
        CommentListCreateView.as_view(),
        name="comments",
    ),

    path(
        "<uuid:post_id>/like/",
        ToggleLikeView.as_view(),
        name="toggle-like",
    ),

    path(
        "initiatives/",
        InitiativeListCreateView.as_view(),
        name="initiative-list-create",
    ),

    path(
        "initiatives/<uuid:pk>/",
        InitiativeDetailView.as_view(),
        name="initiative-detail",
    ),

    path(
        "forum/topics/",
        ForumTopicListCreateView.as_view(),
        name="forum-topic-list",
    ),

    path(
        "forum/topics/<uuid:pk>/",
        ForumTopicDetailView.as_view(),
        name="forum-topic-detail",
    ),

    path(
        "forum/topics/<uuid:topic_id>/replies/",
        ForumReplyListCreateView.as_view(),
        name="forum-replies",
    ),
]

