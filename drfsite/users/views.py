from rest_framework import generics
from django.shortcuts import render
from .models import My_users
from .serializers import MyuserSerializer

class MyuserAPIView(generics.ListAPIView):
    queryset = My_users.objects.all()
    serializer_class = MyuserSerializer



