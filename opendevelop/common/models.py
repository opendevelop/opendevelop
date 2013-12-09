from django.contrib.auth.models import AbstractUser
from django.db import models
import docker


class DockerServer(models.Model):
    _api = None

    name = models.CharField(max_length=32)
    bucket_list = models.CharField(max_length=128,
                                   default='/etc/opendevelop/buckets')
    url = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name
    
    @property
    def api(self):
        if (not self._api):
            base_url = 'http://%s' % self.url
            self._api = docker.Client(base_url, '1.5')
        return self._api


class OpenDevelopUser(AbstractUser):
    is_organization = models.BooleanField()
