from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    username1 = models.CharField(max_length = 100, primary_key=True)
    country = models.CharField(max_length = 40, null=True)
    age = models.IntegerField(null=True)
