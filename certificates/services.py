# certificates/services.py

import os

from django.conf import settings

from .models import Certificate
from .utils import (
    generate_certificate_number,
    generate_qr_code,
)
from .pdf_generator import (
    generate_certificate_pdf,
)

def create_certificate(
    user,
    course,
    score
):

    existing = (
        Certificate.objects.filter(
            user=user,
            course=course
        ).first()
    )

    if existing:
        return existing

    certificate = (
        Certificate.objects.create(
            user=user,
            course=course,
            score=score,
            certificate_number=
                generate_certificate_number()
        )
    )

    qr_path = generate_qr_code(
        certificate
    )

    certificate.qr_code = qr_path

    pdf_directory = os.path.join(
        settings.MEDIA_ROOT,
        "certificates"
    )

    os.makedirs(
        pdf_directory,
        exist_ok=True
    )

    pdf_filename = (
        f"{certificate.certificate_number}.pdf"
    )

    pdf_path = os.path.join(
        pdf_directory,
        pdf_filename
    )

    generate_certificate_pdf(
        certificate,
        pdf_path
    )

    certificate.pdf = (
        f"certificates/{pdf_filename}"
    )

    certificate.save()

    return certificate

