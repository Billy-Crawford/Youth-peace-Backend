# academy/serializers.py

from rest_framework import serializers

from .models import Course, Module, Lesson, Choice, Question, Quiz, LessonProgress


class CourseSerializer(
    serializers.ModelSerializer
):

    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = Course

        fields = (
            "id",
            "title",
            "description",
            "thumbnail",
            "is_published",
            "creator_name",
            "created_at",
        )

        read_only_fields = (
            "id",
            "creator_name",
            "created_at",
        )

    def get_creator_name(
        self,
        obj
    ):
        return (
            f"{obj.created_by.first_name} "
            f"{obj.created_by.last_name}"
        )

class ModuleSerializer(serializers.ModelSerializer):

    course_title = serializers.ReadOnlyField(
        source="course.title"
    )

    class Meta:
        model = Module

        fields = (
            "id",
            "course",
            "course_title",
            "title",
            "order",
        )

        read_only_fields = (
            "id",
            "course_title",
        )

class LessonSerializer(serializers.ModelSerializer):

    module_title = serializers.ReadOnlyField(
        source="module.title"
    )

    class Meta:
        model = Lesson

        fields = (
            "id",
            "module",
            "module_title",
            "title",
            "content",
            "pdf",
            "video_url",
            "order",
        )


        read_only_fields = (
            "id",
            "module_title",
        )

class LessonNestedSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Lesson

        fields = (
            "id",
            "title",
            "content",
            "pdf",
            "video_url",
            "order",
        )


class ModuleNestedSerializer(
    serializers.ModelSerializer
):

    lessons = LessonNestedSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Module

        fields = (
            "id",
            "title",
            "order",
            "lessons",
        )

class CourseDetailSerializer(
    serializers.ModelSerializer
):

    modules = ModuleNestedSerializer(
        many=True,
        read_only=True
    )

    creator_name = serializers.SerializerMethodField()

    quiz_id = serializers.SerializerMethodField()
    quiz_title = serializers.SerializerMethodField()

    class Meta:
        model = Course

        fields = (
            "id",
            "title",
            "description",
            "thumbnail",
            "is_published",
            "creator_name",
            "modules",
            "quiz_id",
            "quiz_title",
            "created_at",
        )

    def get_creator_name(
        self,
        obj
    ):
        return (
            f"{obj.created_by.first_name} "
            f"{obj.created_by.last_name}"
        )

    def get_quiz_id(
        self,
        obj
    ):
        if hasattr(obj, "quiz"):
            return str(obj.quiz.id)

        return None

    def get_quiz_title(
        self,
        obj
    ):
        if hasattr(obj, "quiz"):
            return obj.quiz.title

        return None

# class CourseDetailSerializer(
#     serializers.ModelSerializer
# ):
#
#     modules = ModuleNestedSerializer(
#         many=True,
#         read_only=True
#     )
#
#     creator_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Course
#
#         fields = (
#             "id",
#             "title",
#             "description",
#             "thumbnail",
#             "is_published",
#             "creator_name",
#             "modules",
#             "created_at",
#         )
#
#     def get_creator_name(
#         self,
#         obj
#     ):
#         return (
#             f"{obj.created_by.first_name} "
#             f"{obj.created_by.last_name}"
#         )


class ChoiceSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Choice

        fields = (
            "id",
            "question",
            "choice_text",
            "is_correct",
        )


class QuestionSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Question

        fields = (
            "id",
            "quiz",
            "question_text",
        )


class QuizSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Quiz

        fields = (
            "id",
            "course",
            "title",
            "passing_score",
        )


class ChoicePublicSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Choice

        fields = (
            "id",
            "choice_text",
        )


class QuestionPublicSerializer(
    serializers.ModelSerializer
):

    choices = ChoicePublicSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Question

        fields = (
            "id",
            "question_text",
            "choices",
        )


class QuizDetailSerializer(
    serializers.ModelSerializer
):

    questions = QuestionPublicSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Quiz

        fields = (
            "id",
            "title",
            "passing_score",
            "questions",
        )

class QuizSubmissionSerializer(
    serializers.Serializer
):

    answers = serializers.ListField(
        child=serializers.DictField()
    )

class LessonProgressSerializer(
    serializers.ModelSerializer
):

    lesson_title = serializers.CharField(
        source="lesson.title",
        read_only=True
    )

    class Meta:
        model = LessonProgress

        fields = [
            "id",
            "lesson",
            "lesson_title",
            "completed",
            "completed_at",
        ]



