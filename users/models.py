from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']
    # USERNAME_FIELD is defaults to 'username'

    def __str__(self):
        return self.username
