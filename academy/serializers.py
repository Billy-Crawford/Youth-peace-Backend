# academy/serializers.py

from rest_framework import serializers

from .models import Course, Module, Lesson


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


