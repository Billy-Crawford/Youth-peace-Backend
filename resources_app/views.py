# resources_app/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Resource,
    ResourceFavorite,
)

from .serializers import (
    ResourceSerializer,
    ResourceFavoriteSerializer,
)

from .permissions import (
    IsAdminOrOSC,
    IsOwnerOrAdmin,
)


class ResourceListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = ResourceSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsAdminOrOSC(),
            ]

        return [IsAuthenticated()]

    queryset = Resource.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )


class ResourceDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = ResourceSerializer

    queryset = Resource.objects.all()

    def get_permissions(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:
            return [
                IsAuthenticated(),
                IsOwnerOrAdmin(),
            ]

        return [IsAuthenticated()]


class ToggleFavoriteView(
    APIView
):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        resource_id
    ):

        favorite = (
            ResourceFavorite.objects.filter(
                user=request.user,
                resource_id=resource_id
            ).first()
        )

        if favorite:

            favorite.delete()

            return Response(
                {
                    "favorite": False,
                    "message":
                        "Retiré des favoris"
                }
            )

        ResourceFavorite.objects.create(
            user=request.user,
            resource_id=resource_id
        )

        return Response(
            {
                "favorite": True,
                "message":
                    "Ajouté aux favoris"
            }
        )


class FavoriteListView(
    generics.ListAPIView
):

    serializer_class = (
        ResourceFavoriteSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return (
            ResourceFavorite.objects.filter(
                user=self.request.user
            )
        )

