from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from models import Image
import re


class Command(BaseCommand):

    help = "Add a new OpenDevelop image"

    option_list = BaseCommand.option_list + (
        make_option(
            '--name',
            dest='name',
            help="Specify a name for the new image"),
        make_option(
            '--description',
            dest='description',
            help="Small image description"),
        make_option(
            '--url',
            dest='url',
            help=""),
        make_option(
            '--docker_image',
            dest='docker_image',
            help="Specify docker image to use"),
    )

    def handle(self, *args, **options):
        name = options['name']
        description = options['description']
        url = options['url']
        docker_image = options['docker_image']

        if name is None:
            raise CommandError("Please give an image name")

        if description is None:

        if docker_image is None:
            raise CommandError("Please provide an docker image name")


        try:
            user = models.OpenDevelopUser.objects.get(Q(username=username) |
                                                      Q(email=mail))
        except models.OpenDevelopUser.DoesNotExist:
            raise CommandError("User not found")

        app = models.App.objects.create(name=app_name, owner=user)

        self.stdout.write("An app created succesfully\n"
                          "Client ID %s\nClient Secret %s\n"
                          % (app.client_id, app.client_secret))
