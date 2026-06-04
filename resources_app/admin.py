from django.contrib import admin

from .models import (
    Resource,
    ResourceFavorite,
)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "resource_type",
        "created_by",
        "is_published",
        "created_at",
    )

    list_filter = (
        "resource_type",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(ResourceFavorite)
class ResourceFavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "resource",
        "created_at",
    )


