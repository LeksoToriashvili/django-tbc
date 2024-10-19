from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')))
    last_login = None
    date_joined = None

    def __str__(self):
        return self.username
