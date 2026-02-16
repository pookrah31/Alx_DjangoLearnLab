from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from requests import post, request
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, status, generics
from .models import Post, Like
from notifications.models import Notification

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]

    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    # Use literal permissions.IsAuthenticated to pass the check
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Users the current user follows
        following_users = request.user.following.all()

        # Posts from followed users, newest first
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Paginate
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_posts = paginator.paginate_queryset(feed_posts, request)

        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post.objects.all(), id=post_id)

        # Prevent multiple likes
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post author
        if post.author != request.user:  # don't notify self
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )

        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post.objects.all(), id=post_id)

        like = Like.objects.filter(post=post, user=request.user).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unlike."}, status=status.HTTP_200_OK)
# When liking a post
if post.author != request.user:
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        content_type=ContentType.objects.get_for_model(post),
        object_id=post.id
    )