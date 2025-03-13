from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomSerializer


# Create your views here.
class ListUsers(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer
