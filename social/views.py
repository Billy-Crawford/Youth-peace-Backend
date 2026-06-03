# social/views.py

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from notifications.utils import create_notification
from .models import Post, Comment, Like, Initiative, ForumTopic, ForumReply
from .serializers import PostSerializer, CommentSerializer, InitiativeSerializer, ForumTopicSerializer, \
    ForumReplySerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    queryset = Post.objects.all()

# class PostListCreateView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]
#
#     queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    queryset = Post.objects.all()

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [
#         IsAuthenticated,
#         IsOwnerOrReadOnly,
#     ]
#
#     queryset = Post.objects.all()

class CommentListCreateView(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs["post_id"]
        )

    def perform_create(self, serializer):

        comment = serializer.save(
            author=self.request.user,
            post_id=self.kwargs["post_id"]
        )

        post_author = comment.post.author

        if post_author != self.request.user:

            create_notification(
                user=post_author,
                title="Nouveau commentaire",
                message=(
                    f"{self.request.user.get_full_name()} "
                    f"a commenté votre publication."
                ),
                notification_type="POST",
            )

class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):

        post = Post.objects.get(id=post_id)

        like = Like.objects.filter(
            user=request.user,
            post=post
        ).first()

        if like:
            like.delete()

            return Response(
                {
                    "liked": False,
                    "message": "Like retiré"
                }
            )

        Like.objects.create(
            user=request.user,
            post=post
        )

        return Response(
            {
                "liked": True,
                "message": "Publication likée"
            },
            status=status.HTTP_201_CREATED
        )


class InitiativeListCreateView(generics.ListCreateAPIView):
    serializer_class = InitiativeSerializer
    permission_classes = [IsAuthenticated]

    queryset = Initiative.objects.all()


class InitiativeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InitiativeSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    queryset = Initiative.objects.all()



class ForumTopicListCreateView(generics.ListCreateAPIView):
    serializer_class = ForumTopicSerializer
    permission_classes = [IsAuthenticated]

    queryset = ForumTopic.objects.all()


class ForumTopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ForumTopicSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    queryset = ForumTopic.objects.all()


class ForumReplyListCreateView(generics.ListCreateAPIView):

    serializer_class = ForumReplySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ForumReply.objects.filter(
            topic_id=self.kwargs["topic_id"]
        )

    def perform_create(self, serializer):

        reply = serializer.save(
            author=self.request.user,
            topic_id=self.kwargs["topic_id"]
        )

        topic_author = reply.topic.author

        if topic_author != self.request.user:

            create_notification(
                user=topic_author,
                title="Nouvelle réponse",
                message=(
                    f"{self.request.user.get_full_name()} "
                    f"a répondu à votre sujet."
                ),
                notification_type="FORUM",
            )




