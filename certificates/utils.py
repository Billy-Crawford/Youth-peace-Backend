# certificates/utils.py
import os

import qrcode
from django.conf import settings

from .models import Certificate


def generate_certificate_number():

    year = 2026

    count = (
        Certificate.objects.count()
        + 1
    )

    return (
        f"YP-{year}-{count:06d}"
    )


def generate_certificate_number():

    year = 2026

    count = (
        Certificate.objects.count()
        + 1
    )

    return f"YP-{year}-{count:06d}"


def generate_qr_code(certificate):

    qr_directory = os.path.join(
        settings.MEDIA_ROOT,
        "certificates",
        "qr"
    )

    os.makedirs(
        qr_directory,
        exist_ok=True
    )

    verify_url = (
        f"http://127.0.0.1:8000/"
        f"api/certificates/verify/"
        f"{certificate.certificate_number}/"
    )

    qr = qrcode.make(
        verify_url
    )

    qr_filename = (
        f"{certificate.certificate_number}.png"
    )

    qr_path = os.path.join(
        qr_directory,
        qr_filename
    )

    qr.save(qr_path)

    return (
        f"certificates/qr/{qr_filename}"
    )


