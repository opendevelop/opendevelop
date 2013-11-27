from django.db import models


class Sandbox(models.Model):
    CREATED = 'created'
    RUNNING = 'running'
    TERMINATED = 'terminated'
    STATUSES = ((CREATED, 'Created'),
                (RUNNING, 'Running'),
                (TERMINATED, 'Terminated'))

    slug = models.SlugField(max_length=32)
    owner_app = models.ForeignKey('api.App')
    time = models.DateTimeField(auto_now=True)
    image = models.ForeignKey('images.Image')
    cmd = models.TextField()
    status = models.CharField(choices=STATUSES, max_length=16, default=CREATED)

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
    return_code = models.IntegerField()
    logs = models.TextField()
