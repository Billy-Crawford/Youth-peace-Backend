# # alerts/serializers.py

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
        return f"{obj.reporter.first_name} {obj.reporter.last_name}"

    def validate(self, data):
        # DRF validation correcte
        lat = data.get("latitude")
        lng = data.get("longitude")

        if lat is None or lng is None:
            raise serializers.ValidationError(
                "La localisation (latitude/longitude) est requise."
            )

        return data



# from rest_framework import serializers
#
# from .models import AlertReport
#
#
# class AlertReportSerializer(serializers.ModelSerializer):
#
#     reporter_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = AlertReport
#
#         fields = (
#             "id",
#             "reporter",
#             "reporter_name",
#             "title",
#             "description",
#             "report_type",
#             "location_name",
#             "latitude",
#             "longitude",
#             "photo",
#             "status",
#             "created_at",
#             "updated_at",
#         )
#
#         read_only_fields = (
#             "id",
#             "reporter",
#             "reporter_name",
#             "status",
#             "created_at",
#             "updated_at",
#         )
#
#     def get_reporter_name(self, obj):
#         return (
#             f"{obj.reporter.first_name} "
#             f"{obj.reporter.last_name}"
#         )
#
#
#
#
