from rest_framework import  status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from .models import Project, User, UserProject, ToDo
from .serializer import ProjectSerializer, UserSerializer, UserProjectSerializer, ToDoSerializer
from rest_framework.pagination import LimitOffsetPagination

from collections import namedtuple

class ProjectViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class ProjectParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class UserProjectViewSet(viewsets.ModelViewSet):
    queryset = UserProject.objects.all()
    serializer_class = UserProjectSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ToDoLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


    # def get(self, request):
    #     p = Project.objects.all()
    #     return Response({'posts': ProjectSerializer(p, many=True).data})
    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk=kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method put not allowed"})
    #     try:
    #         instance=Project.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exist"})
    #
    #     serializer=ProjectSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post":serializer.data})

