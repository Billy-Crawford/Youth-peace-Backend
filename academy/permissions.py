# academy/permissions.py

from rest_framework.permissions import BasePermission


class IsAdminOrOSC(BasePermission):

    def has_permission(
        self,
        request,
        view
    ):
        return (
            request.user.is_authenticated
            and request.user.role in [
                "ADMIN",
                "OSC",
            ]
        )


class IsOwnerOrAdmin(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):

        # ADMIN
        if request.user.role == "ADMIN":
            return True

        # OSC propriétaire
        return obj.created_by == request.user

