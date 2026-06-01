# academy/urls.py

from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView, ModuleListView, ModuleCreateView, ModuleDetailView, LessonListView, LessonCreateView,
    LessonDetailView, CourseUpdateDeleteView, QuizCreateView, QuestionCreateView, ChoiceCreateView, QuizDetailView,
    SubmitQuizView, CompleteLessonView, CourseProgressView,
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

    path(
        "quizzes/create/",
        QuizCreateView.as_view(),
        name="quiz-create",
    ),

    path(
        "questions/create/",
        QuestionCreateView.as_view(),
        name="question-create",
    ),

    path(
        "choices/create/",
        ChoiceCreateView.as_view(),
        name="choice-create",
    ),

    path(
        "quizzes/<uuid:pk>/",
        QuizDetailView.as_view(),
        name="quiz-detail",
    ),

    path(
        "quizzes/<uuid:pk>/submit/",
        SubmitQuizView.as_view(),
        name="quiz-submit",
    ),

    path(
        "lessons/<uuid:lesson_id>/complete/",
        CompleteLessonView.as_view(),
        name="lesson-complete",
    ),

    path(
        "courses/<uuid:course_id>/progress/",
        CourseProgressView.as_view(),
        name="course-progress",
    ),
]

