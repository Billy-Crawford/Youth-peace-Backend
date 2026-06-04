# academy/admin.py

from django.contrib import admin

from .models import (
    Course,
    Module,
    Lesson,
    Quiz,
    Question,
    Choice,
    QuizAttempt,
    LessonProgress,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_by",
        "is_published",
        "created_at",
    )
    search_fields = ("title",)
    list_filter = (
        "is_published",
        "created_at",
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "order",
    )
    search_fields = ("title",)
    list_filter = ("course",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "module",
        "order",
    )
    search_fields = ("title",)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "passing_score",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question_text",
        "quiz",
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        "choice_text",
        "question",
        "is_correct",
    )
    list_filter = ("is_correct",)


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "quiz",
        "score",
        "passed",
        "attempted_at",
    )
    list_filter = (
        "passed",
        "attempted_at",
    )


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "lesson",
        "completed",
        "completed_at",
    )



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # affiche 4 champs par défaut
    min_num = 1
    max_num = 10


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "quiz")
    inlines = [ChoiceInline]