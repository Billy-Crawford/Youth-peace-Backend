# certificates/admin.py

from django.contrib import admin

from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "certificate_number",
        "user",
        "course",
        "score",
        "issued_at",
    )

    search_fields = (
        "certificate_number",
        "user__email",
    )

    