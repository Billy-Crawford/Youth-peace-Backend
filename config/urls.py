# config/urls.py

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/posts/", include("social.urls")),
    path("api/messages/", include("messaging.urls")),
    path("api/alerts/",include("alerts.urls")),
    path("api/academy/",include("academy.urls"),),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

