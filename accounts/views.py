# accounts/views.py
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import (
    RegisterSerializer,
    ProfileSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user

# je cree un compte admin pour le test de render + neon + cloudinary
def create_admin(request):
    if not User.objects.filter(email="billy@gmail.com").exists():

        User.objects.create_superuser(
            email="billy@gmail.com",
            password="Admin123456",
            first_name="Billy",
            last_name="Admin",
        )

        return HttpResponse("Superuser created")

    return HttpResponse("Already exists")
