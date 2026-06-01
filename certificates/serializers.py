# certificates/serializers.py

from rest_framework import serializers

from .models import Certificate


class CertificateSerializer(
    serializers.ModelSerializer
):

    course_title = serializers.CharField(
        source="course.title",
        read_only=True
    )

    class Meta:

        model = Certificate

        fields = [
            "id",
            "certificate_number",
            "course_title",
            "score",
            "pdf",
            "issued_at",
        ]


