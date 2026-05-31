# social/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment, Like, Initiative
from .serializers import PostSerializer, CommentSerializer, InitiativeSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    queryset = Post.objects.all()

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs["post_id"]
        )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs["post_id"]
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

