# alerts/serializers.py

from rest_framework import serializers

from .models import AlertReport


class AlertReportSerializer(serializers.ModelSerializer):

    reporter_name = serializers.SerializerMethodField()

    class Meta:
        model = AlertReport

        fields = (
            "id",
            "reporter",
            "reporter_name",
            "title",
            "description",
            "report_type",
            "location_name",
            "latitude",
            "longitude",
            "photo",
            "status",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "reporter",
            "reporter_name",
            "status",
            "created_at",
            "updated_at",
        )

    def get_reporter_name(self, obj):
        return (
            f"{obj.reporter.first_name} "
            f"{obj.reporter.last_name}"
        )



