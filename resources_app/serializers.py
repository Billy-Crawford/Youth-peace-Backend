from rest_framework import serializers

from .models import (
    Resource,
    ResourceFavorite,
)


class ResourceSerializer(
    serializers.ModelSerializer
):

    creator_name = serializers.CharField(
        source="created_by.get_full_name",
        read_only=True
    )

    class Meta:

        model = Resource

        fields = [
            "id",
            "title",
            "description",
            "resource_type",
            "file",
            "external_url",
            "creator_name",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "creator_name",
            "created_at",
        ]


class ResourceFavoriteSerializer(
    serializers.ModelSerializer
):

    resource_title = serializers.CharField(
        source="resource.title",
        read_only=True
    )

    class Meta:

        model = ResourceFavorite

        fields = [
            "id",
            "resource",
            "resource_title",
            "created_at",
        ]

