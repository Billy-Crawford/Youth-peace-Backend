# alerts/permissions.py

from rest_framework.permissions import BasePermission


class IsAdminOrOSC(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.role in [
                "ADMIN",
                "OSC",
            ]
        )