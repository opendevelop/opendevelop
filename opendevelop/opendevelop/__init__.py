from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opendevelop.settings')
from sandboxes.models import Sandbox

CELERY_ACCEPT_CONTENT = ['json']
app = Celery('opendevelop',
        broker='amqp://guest@localhost',
        backend='amqp')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
