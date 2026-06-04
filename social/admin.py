from django.contrib import admin

from .models import (
    Post,
    Comment,
    Like,
    Initiative,
    ForumTopic,
    ForumReply,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "created_at",
    )

    search_fields = (
        "content",
        "author__email",
    )

    list_filter = (
        "created_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "post",
        "created_at",
    )

    search_fields = (
        "content",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "created_at",
    )


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "location",
        "created_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )


@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "created_at",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(ForumReply)
class ForumReplyAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "topic",
        "created_at",
    )

    search_fields = (
        "content",
    )

