from django.db import models
import random


def _random(digits):
    alphabet = '0123456789abcdef'
    result = ''
    for i in range(digits):
        result += random.choice(alphabet)
    return result

def _random_client_id():
    return _random(20)

def _random_client_secret():
    return _random(40)

class App(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=20, default=_random_client_id)
    client_secret = models.CharField(max_length=40,
                                     default=_random_client_secret)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    owner = models.ForeignKey('common.OpenDevelopUser')
    time = models.DateTimeField(auto_now=True)
    homepage = models.URLField()
    description = models.TextField()
    is_active = models.BooleanField()

    def __unicode__(self):
        return self.name
