# social/serializers.py

from rest_framework import serializers
from .models import Post, Comment, Like, Initiative


class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField()

    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "author_name",
            "content",
            "image",
            "likes_count",
            "comments_count",
            "is_liked",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "author",
            "created_at",
            "updated_at",
        )

    def get_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user

        def get_likes_count(self, obj):
            return obj.likes.count()

        def get_comments_count(self, obj):
            return obj.comments.count()

        def get_is_liked(self, obj):
            request = self.context.get("request")

            if not request:
                return False

            if not request.user.is_authenticated:
                return False

            return Like.objects.filter(
                user=request.user,
                post=obj
            ).exists()

        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment

        fields = (
            "id",
            "post",
            "author",
            "author_name",
            "content",
            "created_at",
        )

        read_only_fields = (
            "id",
            "post",
            "author",
            "created_at",
        )

    def get_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user

        return super().create(validated_data)


class InitiativeSerializer(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Initiative

        fields = (
            "id",
            "author",
            "author_name",
            "title",
            "category",
            "description",
            "location",
            "image",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "author",
            "created_at",
            "updated_at",
        )

    def get_author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

