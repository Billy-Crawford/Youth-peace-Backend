# dashboard/views.py

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from accounts.models import User
from academy.models import Course
from resources_app.models import Resource
from social.models import Initiative
from alerts.models import AlertReport

from .permissions import IsOSCOrAdmin

from .serializers import (
    UserListSerializer,
    CourseDashboardSerializer,
    ResourceDashboardSerializer,
    InitiativeDashboardSerializer,
    AlertDashboardSerializer,
)


class OSCStatsView(APIView):

    permission_classes = [
        IsOSCOrAdmin
    ]

    def get(
        self,
        request
    ):

        user = request.user

        if user.role == "ADMIN":

            courses = Course.objects.count()

            resources = Resource.objects.count()

            initiatives = (
                Initiative.objects.count()
            )

            reports = (
                AlertReport.objects.count()
            )

        else:

            courses = (
                Course.objects.filter(
                    created_by=user
                ).count()
            )

            resources = (
                Resource.objects.filter(
                    created_by=user
                ).count()
            )

            initiatives = (
                Initiative.objects.filter(
                    author=user
                ).count()
            )

            reports = (
                AlertReport.objects.count()
            )

        return Response(
            {
                "total_reports":
                    reports,

                "pending_reports":
                    AlertReport.objects.filter(
                        status="PENDING"
                    ).count(),

                "resolved_reports":
                    AlertReport.objects.filter(
                        status="RESOLVED"
                    ).count(),

                "initiatives":
                    initiatives,

                "courses":
                    courses,

                "resources":
                    resources,
            }
        )


class UserListView(
    ListAPIView
):

    serializer_class = (
        UserListSerializer
    )

    permission_classes = [
        IsOSCOrAdmin
    ]

    queryset = User.objects.filter(
        role="JEUNE"
    )


class DashboardCourseListView(
    ListAPIView
):

    serializer_class = (
        CourseDashboardSerializer
    )

    permission_classes = [
        IsOSCOrAdmin
    ]

    def get_queryset(self):

        if (
            self.request.user.role
            == "ADMIN"
        ):
            return Course.objects.all()

        return Course.objects.filter(
            created_by=self.request.user
        )


class DashboardResourceListView(
    ListAPIView
):

    serializer_class = (
        ResourceDashboardSerializer
    )

    permission_classes = [
        IsOSCOrAdmin
    ]

    def get_queryset(self):

        if (
            self.request.user.role
            == "ADMIN"
        ):
            return Resource.objects.all()

        return Resource.objects.filter(
            created_by=self.request.user
        )


class DashboardInitiativeListView(
    ListAPIView
):

    serializer_class = (
        InitiativeDashboardSerializer
    )

    permission_classes = [
        IsOSCOrAdmin
    ]

    def get_queryset(self):

        if (
            self.request.user.role
            == "ADMIN"
        ):
            return Initiative.objects.all()

        return Initiative.objects.filter(
            author=self.request.user
        )


class DashboardAlertListView(
    ListAPIView
):

    serializer_class = (
        AlertDashboardSerializer
    )

    permission_classes = [
        IsOSCOrAdmin
    ]

    queryset = AlertReport.objects.all()

