# academy/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from certificates.services import create_certificate
from .models import Course, Module, Lesson, Quiz, Question, Choice, QuizAttempt, LessonProgress
from .serializers import (
    CourseSerializer, ModuleSerializer, LessonSerializer, CourseDetailSerializer, QuizSerializer, QuestionSerializer,
    ChoiceSerializer, QuizDetailSerializer, QuizSubmissionSerializer, LessonProgressSerializer,
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



class QuizCreateView(
    generics.CreateAPIView
):

    serializer_class = QuizSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Quiz.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )

class QuestionCreateView(
    generics.CreateAPIView
):

    serializer_class = QuestionSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Question.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )


class ChoiceCreateView(
    generics.CreateAPIView
):

    serializer_class = ChoiceSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdminOrOSC,
    ]

    queryset = Choice.objects.all()

    def perform_create(
        self,
        serializer
    ):
        serializer.save(
            created_by=self.request.user
        )


class QuizDetailView(
    generics.RetrieveAPIView
):

    serializer_class = QuizDetailSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Quiz.objects.all()



class SubmitQuizView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        pk
    ):

        serializer = QuizSubmissionSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        quiz = get_object_or_404(
            Quiz,
            pk=pk
        )

        course = quiz.course

        total_lessons = Lesson.objects.filter(
            module__course=course
        ).count()

        completed_lessons = LessonProgress.objects.filter(
            user=request.user,
            lesson__module__course=course
        ).count()

        if completed_lessons < total_lessons:
            return Response(
                {
                    "error": (
                        "Vous devez terminer "
                        "toutes les leçons avant "
                        "de passer le quiz."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        answers = serializer.validated_data[
            "answers"
        ]

        total_questions = (
            quiz.questions.count()
        )

        correct_answers = 0

        for answer in answers:

            question_id = answer.get(
                "question_id"
            )

            choice_id = answer.get(
                "choice_id"
            )

            try:

                choice = Choice.objects.get(
                    id=choice_id,
                    question_id=question_id
                )

                if choice.is_correct:
                    correct_answers += 1

            except Choice.DoesNotExist:
                pass

        score = 0

        if total_questions > 0:

            score = int(
                (
                    correct_answers
                    / total_questions
                ) * 100
            )

        passed = (
            score >= quiz.passing_score
        )

        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            passed=passed
        )

        certificate = None

        if passed:
            certificate = (
                create_certificate(
                    request.user,
                    quiz.course,
                    score
                )
            )

        return Response(
            {
                "attempt_id":
                    str(attempt.id),

                "score":
                    score,

                "passed":
                    passed,

                "passing_score":
                    quiz.passing_score,

                "correct_answers":
                    correct_answers,

                "total_questions":
                    total_questions,

                "certificate":
                    (
                        certificate.certificate_number
                        if certificate
                        else None
                    )
            },
            status=status.HTTP_200_OK
        )



class CompleteLessonView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        lesson_id
    ):

        lesson = get_object_or_404(
            Lesson,
            id=lesson_id
        )

        progress, created = (
            LessonProgress.objects.get_or_create(
                user=request.user,
                lesson=lesson
            )
        )

        serializer = (
            LessonProgressSerializer(
                progress
            )
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )



class CourseProgressView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request,
        course_id
    ):

        course = get_object_or_404(
            Course,
            id=course_id
        )

        total_lessons = Lesson.objects.filter(
            module__course=course
        ).count()

        completed_lessons = (
            LessonProgress.objects.filter(
                user=request.user,
                lesson__module__course=course
            ).count()
        )

        percentage = 0

        if total_lessons > 0:

            percentage = round(
                (
                    completed_lessons
                    / total_lessons
                ) * 100,
                2
            )

        return Response({
            "course": course.title,
            "total_lessons": total_lessons,
            "completed_lessons": completed_lessons,
            "progress_percentage": percentage,
            "completed": (
                completed_lessons
                == total_lessons
                and total_lessons > 0
            )
        })

