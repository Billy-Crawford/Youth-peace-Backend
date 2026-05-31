# alerts/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AlertReport
from .permissions import IsAdminOrOSC
from .serializers import AlertReportSerializer


class AlertReportListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = AlertReportSerializer
    permission_classes = [IsAuthenticated]

    # alerts/views.py

    def get_queryset(self):

        queryset = AlertReport.objects.all()

        report_type = self.request.query_params.get(
            "report_type"
        )

        status_filter = self.request.query_params.get(
            "status"
        )

        if report_type:
            queryset = queryset.filter(
                report_type=report_type
            )

        if status_filter:
            queryset = queryset.filter(
                status=status_filter
            )

        return queryset

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            reporter=self.request.user
        )


class AlertReportDetailView(
    generics.RetrieveAPIView
):

    serializer_class = AlertReportSerializer
    permission_classes = [IsAuthenticated]

    queryset = AlertReport.objects.all()


class UpdateReportStatusView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]


    def patch(
            self,
            request,
            report_id
    ):
        report = AlertReport.objects.get(
            id=report_id
        )

        new_status = request.data.get(
            "status"
        )

        allowed_statuses = [
            "PENDING",
            "IN_REVIEW",
            "RESOLVED",
        ]

        if new_status not in allowed_statuses:
            return Response(
                {
                    "error":
                        "Statut invalide."
                },
                status=400,
            )

        report.status = new_status

        report.save()

        return Response(
            {
                "message":
                    "Statut mis à jour."
            }
        )

        report = AlertReport.objects.get(
            id=report_id
        )

        new_status = request.data.get(
            "status"
        )

        report.status = new_status

        report.save()

        return Response(
            {
                "message":
                "Statut mis à jour."
            }
        )


class AlertStatisticsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response(
            {
                "total_reports":
                    AlertReport.objects.count(),

                "total_tensions":
                    AlertReport.objects.filter(
                        report_type="TENSION"
                    ).count(),

                "total_vbg":
                    AlertReport.objects.filter(
                        report_type="VBG"
                    ).count(),

                "total_initiatives":
                    AlertReport.objects.filter(
                        report_type="INITIATIVE"
                    ).count(),

                "pending_reports":
                    AlertReport.objects.filter(
                        status="PENDING"
                    ).count(),

                "resolved_reports":
                    AlertReport.objects.filter(
                        status="RESOLVED"
                    ).count(),
            }
        )

