from django.db import models

class Sandbox(models.Model):
	CREATED = 'created'
	RUNNING = 'running'
	TERMINATED = 'terminated'
	STATUSES = (
                    (CREATED, 'Created'),
                    (RUNNING, 'Running'),
                    (TERMINATED, 'Terminated')
               )

	slug = models.SlugField(max_length=32)
	owner_app = models.ForeignKey('api.App')
	time = models.DateTimeField(auto_now=True)
	image = models.ForeignKey('images.Image')
	cmd = models.TextField()
	status = models.CharField(choices=STATUSES, max_length=16, default=CREATED)


class SandboxLog(models.Model):
    sandbox = models.ForeignKey('sandboxes.Sandbox')
    return_code = models.IntegerField()
    logs = models.TextField()
