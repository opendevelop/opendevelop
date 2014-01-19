from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from images.models import Image
from common.models import DockerServer
import re


class Command(BaseCommand):

    help = "Add a new OpenDevelop Server"

    option_list = BaseCommand.option_list + (
        make_option(
            '--name',
            dest='name',
            help="Specify a name for the new server"),
        make_option(
            '--url',
            dest='url',
            help="Specify a url to connect for management. Default is "
                  "unixL//run/docker.sock"),
        make_option(
            '--buckets',
            dest='buckets',
            help="Specify directory to place the created bucketsi. Default is "
                  "/etc/opendevelop/buckets"),
    )

    def handle(self, *args, **options):
        name = options['name']
        url = options['url']
        buckets_dir = options['buckets']

        self.stdout.write("Succesully created server\n")
