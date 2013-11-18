from django.db import models


class App(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=20)
    client_secret = models.CharField(max_length=40)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    owner = models.ForeignKey('common.OpenDevelopUser')
    time = models.DateTimeField(auto_now=True)
    homepage = models.URLField()
    description = models.TextField()
    is_active = models.BooleanField()
