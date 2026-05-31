# messaging/views.py

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from .models import Conversation, Message
from .serializers import (
    ConversationSerializer,
    MessageSerializer, CreateConversationSerializer,
)


class ConversationListCreateView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):

        if self.request.method == "POST":
            return CreateConversationSerializer

        return ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(
            participants=self.request.user
        )

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        recipient_id = serializer.validated_data[
            "recipient_id"
        ]

        try:
            recipient = User.objects.get(
                id=recipient_id
            )

        except User.DoesNotExist:

            return Response(
                {
                    "detail": "Utilisateur introuvable."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        existing_conversations = (
            Conversation.objects.filter(
                participants=request.user
            )
        )

        for conversation in existing_conversations:

            participants = list(
                conversation.participants.all()
            )

            if (
                len(participants) == 2
                and request.user in participants
                and recipient in participants
            ):
                return Response(
                    ConversationSerializer(
                        conversation,
                        context={"request": request}
                    ).data
                )

        conversation = Conversation.objects.create()

        conversation.participants.add(
            request.user
        )

        conversation.participants.add(
            recipient
        )

        return Response(
            ConversationSerializer(
                conversation,
                context={"request": request}
            ).data,
            status=status.HTTP_201_CREATED,
        )


class ConversationDetailView(generics.RetrieveAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    queryset = Conversation.objects.all()


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(
            conversation_id=self.kwargs["conversation_id"]
        )

    def perform_create(self, serializer):
        serializer.save(
            sender=self.request.user,
            conversation_id=self.kwargs["conversation_id"]
        )

class MarkConversationAsReadView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id):

        Message.objects.filter(
            conversation_id=conversation_id,
            is_read=False,
        ).exclude(
            sender=request.user
        ).update(
            is_read=True
        )

        return Response(
            {
                "message": "Messages marqués comme lus."
            }
        )



