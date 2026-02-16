from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.
class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Unread notifications first, then read, newest first
        return Notification.objects.filter(
            recipient=self.request.user
        ).order_by('-timestamp')