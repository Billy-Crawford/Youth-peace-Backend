# academy/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Module, Lesson, Quiz, Question, Choice, QuizAttempt
from .serializers import (
    CourseSerializer, ModuleSerializer, LessonSerializer, CourseDetailSerializer, QuizSerializer, QuestionSerializer,
    ChoiceSerializer, QuizDetailSerializer, QuizSubmissionSerializer,
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

        return Response(
            {
                "attempt_id": str(
                    attempt.id
                ),
                "score": score,
                "passed": passed,
                "passing_score":
                    quiz.passing_score,
                "correct_answers":
                    correct_answers,
                "total_questions":
                    total_questions,
            },
            status=status.HTTP_200_OK
        )




