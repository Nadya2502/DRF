from rest_framework import serializers
from django.shortcuts import render
from .models import My_users



class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_users
        fields = '__all__'