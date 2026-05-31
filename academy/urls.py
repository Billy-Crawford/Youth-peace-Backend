# academy/urls.py

from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView, ModuleListView, ModuleCreateView, ModuleDetailView, LessonListView, LessonCreateView,
    LessonDetailView, CourseUpdateDeleteView,
)

urlpatterns = [

    path(
        "courses/",
        CourseListView.as_view(),
        name="course-list",
    ),

    path(
        "courses/create/",
        CourseCreateView.as_view(),
        name="course-create",
    ),

    path(
        "courses/<uuid:pk>/",
        CourseDetailView.as_view(),
        name="course-detail",
    ),

    path(
        "modules/",
        ModuleListView.as_view(),
        name="module-list",
    ),

    path(
        "modules/create/",
        ModuleCreateView.as_view(),
        name="module-create",
    ),

    path(
        "modules/<uuid:pk>/",
        ModuleDetailView.as_view(),
        name="module-detail",
    ),

    path(
        "lessons/",
        LessonListView.as_view(),
        name="lesson-list",
    ),

    path(
        "lessons/create/",
        LessonCreateView.as_view(),
        name="lesson-create",
    ),

    path(
        "lessons/<uuid:pk>/",
        LessonDetailView.as_view(),
        name="lesson-detail",
    ),

    path(
        "courses/manage/<uuid:pk>/",
        CourseUpdateDeleteView.as_view(),
        name="course-manage",
    ),
]

