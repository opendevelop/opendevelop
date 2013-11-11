from django.contrib.auth.models import AbstractUser
from django.db import models

class DockerServer(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=64)

class OpenDevelopUser(AbstractUser):
    is_organization = models.BooleanField()
