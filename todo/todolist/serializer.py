from rest_framework import fields, serializers
from .models import Project, User, UserProject , ToDo




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Project
        fields = "__all__"

class UserProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer
    project = ProjectSerializer
    class Meta:
        model = UserProject
        fields = "__all__"

class ToDoSerializer(serializers.ModelSerializer):
    user = UserSerializer
    project = ProjectSerializer
    class Meta:
        model = ToDo
        fields = "__all__"