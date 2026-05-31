# alerts/urls.py

from django.urls import path

from .views import (
    AlertReportListCreateView,
    AlertReportDetailView,
    UpdateReportStatusView, AlertStatisticsView,
)

urlpatterns = [

    path(
        "reports/",
        AlertReportListCreateView.as_view(),
        name="report-list-create",
    ),

    path(
        "reports/<uuid:pk>/",
        AlertReportDetailView.as_view(),
        name="report-detail",
    ),

    path(
        "reports/<uuid:report_id>/status/",
        UpdateReportStatusView.as_view(),
        name="report-status",
    ),

    path(
        "statistics/",
        AlertStatisticsView.as_view(),
        name="alert-statistics",
    ),
]



