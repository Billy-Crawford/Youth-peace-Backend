# alerts/models.py

import uuid

from django.db import models
from django.conf import settings


class AlertReport(models.Model):

    TYPE_CHOICES = (
        ("TENSION", "Tension"),
        ("VBG", "Violence Basée sur le Genre"),
        ("INITIATIVE", "Initiative"),
    )

    STATUS_CHOICES = (
        ("PENDING", "En attente"),
        ("IN_REVIEW", "En cours"),
        ("RESOLVED", "Résolu"),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reports",
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    report_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    location_name = models.CharField(
        max_length=255
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
    )

    photo = models.ImageField(
        upload_to="alerts/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

