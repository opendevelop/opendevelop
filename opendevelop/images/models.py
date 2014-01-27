from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Image(models.Model):
    """
    This class defines the Image model. Each sandbox should be created with an
    Image as a base. Each Image should be have a valid counterpart to every
    Docker server connected to OpenDevelop
    """
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    description = models.TextField()
    url = models.URLField(max_length=64, blank=True, null=True, default='')
    docker_image_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    @receiver(pre_save, sender='Image')
    def my_callback(sender, instance, *args, **kwargs):
            instance.slug = slugify(instance.name)
