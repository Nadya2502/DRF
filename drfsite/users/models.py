from django.db import models

class My_users(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    mail = models.CharField(max_length=50, unique=True)

