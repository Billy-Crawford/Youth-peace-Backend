# certificates/models.py

import uuid

from django.db import models
from django.conf import settings


class Certificate(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    course = models.ForeignKey(
        "academy.Course",
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    certificate_number = models.CharField(
        max_length=50,
        unique=True
    )

    score = models.PositiveIntegerField()

    pdf = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    qr_code = models.ImageField(
        upload_to="certificates/qr/",
        blank=True,
        null=True
    )

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-issued_at"]

    def __str__(self):
        return self.certificate_number

