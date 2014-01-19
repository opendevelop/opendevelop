from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from images.models import Image
from common.models import DockerServer
import re
import docker

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
        print servers
        get_repos = lambda x : x['Repository']
        for server in servers:
            client = server.api
            print client.base_url
            images = client.images()
            repos = map(get_repos, images)
            if not(name in images):
                print docker_image
                client.pull(docker_image)
                print "Image not found in server %s. Downloading ...\n" % server.name
            else:
                print "Image in server %s.\n" % server.name

        try:
            user = models.OpenDevelopUser.objects.get(Q(username=username) |
                                                      Q(email=mail))
        except models.OpenDevelopUser.DoesNotExist:
            raise CommandError("User not found")

        app = models.App.objects.create(name=app_name, owner=user)

        self.stdout.write("An app created succesfully\n"
                          "Client ID %s\nClient Secret %s\n"
                          % (app.client_id, app.client_secret))
