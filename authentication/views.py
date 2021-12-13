from django.shortcuts import render
from rest_framework import viewsets
from authentication.models import CustomUser

from authentication.serializers import CustomUserSerializer
# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filterset_fields = ['is_active']
    search_fields = ['username', 'email']

