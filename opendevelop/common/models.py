from django.db import models

class DockerServer(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
