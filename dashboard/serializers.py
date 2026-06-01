# dashboard/serializers.py

from rest_framework import serializers

from accounts.models import User
from academy.models import Course
from alerts.models import AlertReport
from resources_app.models import Resource
from social.models import Initiative



class UserListSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "created_at",
        ]


class CourseDashboardSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Course

        fields = [
            "id",
            "title",
            "created_at",
        ]


class ResourceDashboardSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Resource

        fields = [
            "id",
            "title",
            "resource_type",
            "created_at",
        ]


class InitiativeDashboardSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Initiative

        fields = [
            "id",
            "title",
            "category",
            "created_at",
        ]


class AlertDashboardSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = AlertReport

        fields = [
            "id",
            "title",
            "report_type",
            "status",
            "created_at",
        ]