from django.db import models
import random

def _random_slug():
    alphabet = '0123456789abcdef'
    result = ''
    for i in range(16):
        result += random.choice(alphabet)
    return result

class Sandbox(models.Model):
    CREATED = 'created'
    RUNNING = 'running'
    TERMINATED = 'terminated'
    STATUSES = ((CREATED, 'Created'),
                (RUNNING, 'Running'),
                (TERMINATED, 'Terminated'))

    slug = models.SlugField(max_length=32, default=_random_slug)
    owner_app = models.ForeignKey('api.App')
    time = models.DateTimeField(auto_now=True)
    image = models.ForeignKey('images.Image')
    docker_server = models.ForeignKey('common.DockerServer', null=True)
    container_id = models.SlugField(max_length=80, null=True)
    cmd = models.TextField()
    status = models.CharField(choices=STATUSES, max_length=16, default=CREATED)

    def __unicode__(self):
        return self.slug

    def to_dict(self):
        d = {}
        d['image'] = self.image.slug
        d['cmd'] = self.cmd
        d['status'] = self.status
        try:
            d['return_code'] = self.log.return_code
            d['logs'] = self.log.logs
        except:
            d['return_code'] = None
            d['logs'] = None
        return d


class SandboxLog(models.Model):
    sandbox = models.OneToOneField('sandboxes.Sandbox', related_name="log")
    return_code = models.IntegerField(null=True, blank=True)
    logs = models.TextField()

    def __unicode__(self):
        return self.sandbox.slug
