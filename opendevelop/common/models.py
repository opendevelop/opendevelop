from django.db import models
import docker


class DockerServer(models.Model):
    _api = None

    name = models.CharField(max_length=32)
    bucket_list = models.CharField(max_length=128,
                                   default='/etc/opendevelop/buckets')
    url = models.CharField(max_length=64, default='unix://run/docker.sock')

    def __unicode__(self):
        return self.name

    @property
    def api(self):
        if (not self._api):
            self._api = docker.Client(self.url)
        return self._api

class OpenDevelopUser(AbstractUser):
    is_organization = models.BooleanField(default=False)
