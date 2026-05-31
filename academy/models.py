# academy/models.py

import uuid

from django.db import models
from django.conf import settings


class Course(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Module(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules"
    )

    title = models.CharField(
        max_length=255
    )

    order = models.PositiveIntegerField(
        default=1
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="academy_modules",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Lesson(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    pdf = models.FileField(
        upload_to="lessons/",
        blank=True,
        null=True
    )

    video_url = models.URLField(
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=1
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="academy_lessons",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title



class Quiz(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name="quiz"
    )

    title = models.CharField(
        max_length=255
    )

    passing_score = models.PositiveIntegerField(
        default=70
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Question(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_text = models.TextField()

    def __str__(self):
        return self.question_text[:50]


class Choice(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    choice_text = models.CharField(
        max_length=255
    )

    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.choice_text


class QuizAttempt(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_attempts"
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    score = models.PositiveIntegerField(
        default=0
    )

    passed = models.BooleanField(
        default=False
    )

    attempted_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-attempted_at"]


