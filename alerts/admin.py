from django.contrib import admin

from .models import AlertReport


@admin.register(AlertReport)
class AlertReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "report_type",
        "reporter",
        "location_name",
        "status",
        "created_at",
    )

    list_filter = (
        "report_type",
        "status",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "location_name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

