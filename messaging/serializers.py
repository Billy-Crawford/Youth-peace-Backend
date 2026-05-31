# messaging/serializers.py

from rest_framework import serializers

from .models import Conversation, Message
from accounts.models import User


class ConversationSerializer(serializers.ModelSerializer):

    participants_names = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation

        fields = (
            "id",
            "participants",
            "participants_names",
            "last_message",
            "unread_count",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    def get_participants_names(self, obj):
        return [
            f"{user.first_name} {user.last_name}"
            for user in obj.participants.all()
        ]

    def get_last_message(self, obj):
        last_message = obj.messages.order_by(
            "-created_at"
        ).first()

        if not last_message:
            return None

        return {
            "content": last_message.content,
            "sender_name": (
                f"{last_message.sender.first_name} "
                f"{last_message.sender.last_name}"
            ),
            "created_at": last_message.created_at,
        }

    def get_unread_count(self, obj):
        user = self.context.get("request").user

        return obj.messages.filter(
            is_read=False
        ).exclude(
            sender=user
        ).count()


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SerializerMethodField()

    class Meta:
        model = Message

        fields = (
            "id",
            "conversation",
            "sender",
            "sender_name",
            "content",
            "is_read",
            "created_at",
        )

        read_only_fields = (
            "id",
            "conversation",
            "sender",
            "is_read",
            "created_at",
        )

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"


class CreateConversationSerializer(serializers.Serializer):
    recipient_id = serializers.UUIDField()


