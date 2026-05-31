# academy/views.py

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Course, Module, Lesson
from .serializers import (
    CourseSerializer, ModuleSerializer, LessonSerializer, CourseDetailSerializer,
)
from .permissions import (
    IsAdminOrOSC, IsOwnerOrAdmin,
)


class CourseListView(
    generics.ListAPIView
):

    serializer_class = CourseSerializer
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Course.objects.all()


class CourseDetailView(
    generics.RetrieveAPIView
):

    serializer_class = CourseDetailSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Course.objects.all()


class CourseCreateView(
    generics.CreateAPIView
):

    serializer_class = CourseSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Course.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )

class ModuleListView(
    generics.ListAPIView
):

    serializer_class = ModuleSerializer
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Module.objects.all()


class ModuleDetailView(
    generics.RetrieveAPIView
):

    serializer_class = ModuleSerializer
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Module.objects.all()


class ModuleCreateView(
    generics.CreateAPIView
):

    serializer_class = ModuleSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Module.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )


class LessonListView(
    generics.ListAPIView
):

    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Lesson.objects.all()


class LessonDetailView(
    generics.RetrieveAPIView
):

    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated
    ]

    queryset = Lesson.objects.all()


class LessonCreateView(
    generics.CreateAPIView
):

    serializer_class = LessonSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Lesson.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )


class CourseUpdateDeleteView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CourseSerializer

    permission_classes = [
        IsAuthenticated,
        IsOwnerOrAdmin,
    ]

    queryset = Course.objects.all()


