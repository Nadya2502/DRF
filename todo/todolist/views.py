from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Project, User, UserProject, ToDo
from .serializer import ProjectSerializer, UserSerializer, UserProjectSerializer, ToDoSerializer

from collections import namedtuple

class ProjectAPIView(APIView):
    def get(self, request):
        p = Project.objects.all()
        return Response({'posts': ProjectSerializer(p, many=True).data})
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk=kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})
        try:
            instance=Project.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer=ProjectSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

