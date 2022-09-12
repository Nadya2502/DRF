from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url =  models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    mail = models.CharField(max_length=50, unique=True)

    def __init__(self, name, birthday_year):
        self.name = name

        self.date_of_birth = birthday_year

    def __str__(self):
        return self.name

class UserProject(models.Model):
    user = models.ManyToManyField(User)
    project = models.ManyToManyField(Project)

class ToDo(models.Model):
    project = models.ManyToManyField(Project)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __init__(self, text, user):
        self.text = text

        self.user = user