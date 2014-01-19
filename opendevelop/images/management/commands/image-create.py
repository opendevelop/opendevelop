from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from images.models import Image
from common.models import DockerServer
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
            raise CommandError("Please give a description")

        if docker_image is None:
            raise CommandError("Please provide an docker image name")

        #check all docker servers for the image
        #if not there download it
        servers = DockerServer.objects.all()
        get_repos = lambda x: x['Repository']
        for server in servers:
            client = server.api
            images = client.images()
            repos = map(get_repos, images)
            if not(docker_image in repos):
                print "Image not found in server %s. Downloading ...\n" % \
                      server.name
                response = client.pull(docker_image)
                if "error" in response:
                    raise CommandError("There is no such docker image")
            else:
                print "Image found in server %s.\n" % server.name

        image = Image.objects.create(name=name, description=description,
                                     docker_image_name=docker_image)

        self.stdout.write("Image %s created succesfully\n" % image)
