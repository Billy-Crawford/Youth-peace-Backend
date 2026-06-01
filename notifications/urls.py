# notifications/urls.py

from django.urls import path

from .views import (
    NotificationListView,
    UnreadCountView,
    MarkNotificationReadView,
    MarkAllNotificationsReadView,
)

urlpatterns = [
    path(
        "",
        NotificationListView.as_view()
    ),

    path(
        "unread-count/",
        UnreadCountView.as_view()
    ),

    path(
        "<uuid:pk>/read/",
        MarkNotificationReadView.as_view()
    ),

    path(
        "read-all/",
        MarkAllNotificationsReadView.as_view()
    ),
]

