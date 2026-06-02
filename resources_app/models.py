# resources_app/models.py

import uuid

from django.db import models
from django.conf import settings


class Resource(models.Model):

    RESOURCE_TYPES = (
        ("PDF", "PDF"),
        ("VIDEO", "Vidéo"),
        ("PODCAST", "Podcast"),
        ("ARTICLE", "Article"),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resources",
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPES,
    )

    file = models.FileField(
        upload_to="resources/",
        null=True,
        blank=True,
    )

    external_url = models.URLField(
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        upload_to="resources/thumbnails/",
        blank=True,
        null=True,
    )

    is_published = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ResourceFavorite(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = (
            "user",
            "resource",
        )



