# certificates/serializers.py
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

class CertificateDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CertificateSerializer
    lookup_field = "certificate_number"

    queryset = Certificate.objects.all()


class CertificateDownloadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, certificate_number):
        certificate = get_object_or_404(
            Certificate,
            certificate_number=certificate_number,
            user=request.user
        )

        if not certificate.pdf:
            return Response(
                {"error": "PDF introuvable"},
                status=404
            )

        return FileResponse(
            certificate.pdf.open("rb"),
            content_type="application/pdf",
            filename=f"{certificate.certificate_number}.pdf"
        )

