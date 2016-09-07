from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserInfo(AbstractUser):
    cnic=models.CharField(max_length=11)
    category=models.CharField(max_length=20)
    secretque=models.CharField(max_length=200)
    secretans=models.CharField(max_length=200)
    expertise=models.CharField(max_length=50)
    shopaffliation=models.CharField(max_length=100)

    def  __str__(self):
        return self.username

