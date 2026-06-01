# certificates/pdf_generator.py

import os

from django.conf import settings

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Image,
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_certificate_pdf(
    certificate,
    pdf_path,
):

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4)
    )

    styles = getSampleStyleSheet()

    elements = []

    logo_path = os.path.join(
        settings.MEDIA_ROOT,
        "branding",
        "yyp-rbg.png"
    )

    signature_path = os.path.join(
        settings.MEDIA_ROOT,
        "branding",
        "signature.PNG"
    )

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=120,
            height=120
        )

        elements.append(logo)

    elements.append(
        Paragraph(
            "<b>CERTIFICAT DE RÉUSSITE</b>",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Ce certificat est décerné à",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            (
                f"<b>"
                f"{certificate.user.first_name} "
                f"{certificate.user.last_name}"
                f"</b>"
            ),
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            (
                "Pour avoir suivi avec succès "
                f"la formation "
                f"<b>{certificate.course.title}</b>"
            ),
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    elements.append(
        Paragraph(
            (
                f"Score obtenu : "
                f"{certificate.score}%"
            ),
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            (
                f"Numéro : "
                f"{certificate.certificate_number}"
            ),
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 40)
    )

    if os.path.exists(signature_path):

        signature = Image(
            signature_path,
            width=150,
            height=60
        )

        elements.append(signature)

    elements.append(
        Paragraph(
            "Signature officielle YouthPeace",
            styles["Normal"]
        )
    )

    doc.build(elements)

