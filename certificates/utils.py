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



def generate_qr_code(certificate):
    import qrcode
    from io import BytesIO
    from django.core.files.base import ContentFile

    verify_url = (
        f"https://youth-peace-backend.onrender.com/api/certificates/verify/"
        f"{certificate.certificate_number}/"
    )

    qr = qrcode.make(verify_url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    file_name = f"{certificate.certificate_number}.png"

    # IMPORTANT: upload via Django storage (Cloudinary)
    certificate.qr_code.save(
        file_name,
        ContentFile(buffer.getvalue()),
        save=False
    )

    return certificate.qr_code


