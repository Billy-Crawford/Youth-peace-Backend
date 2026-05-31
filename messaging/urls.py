# messaging/urls.py

from django.urls import path

from .views import (
    ConversationListCreateView,
    ConversationDetailView,
    MessageListCreateView, MarkConversationAsReadView,
)

urlpatterns = [
    path(
        "conversations/",
        ConversationListCreateView.as_view(),
        name="conversation-list",
    ),

    path(
        "conversations/<uuid:pk>/",
        ConversationDetailView.as_view(),
        name="conversation-detail",
    ),

    path(
        "conversations/<uuid:conversation_id>/messages/",
        MessageListCreateView.as_view(),
        name="messages",
    ),

    path(
        "conversations/<uuid:conversation_id>/read/",
        MarkConversationAsReadView.as_view(),
        name="conversation-read",
    ),
]

