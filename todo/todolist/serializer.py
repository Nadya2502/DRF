from rest_framework import fields, serializers
from .models import Project, User, UserProject , ToDo

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name", instance.name)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'

class UserProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer
    project = ProjectSerializer
    class Meta:
        model  = UserProject
        fields = '__all__'

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer
    project = ProjectSerializer
    class Meta:
        model  = ToDo
        fields = '__all__'