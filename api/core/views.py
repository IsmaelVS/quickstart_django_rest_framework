from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
