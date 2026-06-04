# certificates/urls.py

from django.urls import path

from .serializers import CertificateDetailView, CertificateDownloadView
from .views import (
    MyCertificatesView, VerifyCertificateView,
)

urlpatterns = [

    path(
        "my-certificates/",
        MyCertificatesView.as_view(),
        name="my-certificates"
    ),

    path(
        "verify/<str:certificate_number>/",
        VerifyCertificateView.as_view(),
        name="verify-certificate",
    ),

    path("<str:certificate_number>/", CertificateDetailView.as_view()),
    path("<str:certificate_number>/download/", CertificateDownloadView.as_view()),

]

