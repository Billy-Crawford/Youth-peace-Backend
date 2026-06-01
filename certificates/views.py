# certificates/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Certificate
from .serializers import CertificateSerializer


class MyCertificatesView(
    generics.ListAPIView
):

    serializer_class = (
        CertificateSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Certificate.objects.filter(
            user=self.request.user
        )

class VerifyCertificateView(
    APIView
):

    permission_classes = []

    authentication_classes = []

    def get(
        self,
        request,
        certificate_number
    ):

        certificate = get_object_or_404(
            Certificate,
            certificate_number=
            certificate_number
        )

        return Response({
            "valid": True,
            "certificate_number":
                certificate.certificate_number,
            "student":
                (
                    f"{certificate.user.first_name} "
                    f"{certificate.user.last_name}"
                ),
            "course":
                certificate.course.title,
            "score":
                certificate.score,
            "issued_at":
                certificate.issued_at,
        })



