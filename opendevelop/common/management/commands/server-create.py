from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from common.models import DockerServer

class Command(BaseCommand):

    help = 'Add a new OpenDevelop Server'

    option_list = BaseCommand.option_list + (
        make_option(
            '--name',
            dest='name',
            help='Specify a name for the new server'),
        make_option(
            '--url',
            dest='url',
            help='Specify a url to connect for management. Default is '
            'unix://run/docker.sock'),
        make_option(
            '--buckets',
            dest='buckets',
            help='Specify directory to place the created buckets. Default is '
                  '/etc/opendevelop/buckets'),
    )

    def handle(self, *args, **options):
        name = options['name']
        url = options['url']
        buckets_dir = options['buckets']

        args = dict()
        if name is None:
            raise CommandError('Please specify a name for the new server')
        args['name'] = name

        if url:
            args['url'] = url

        if buckets_dir:
            args['bucket_list']=buckets_dir

        server = DockerServer.objects.create(**args)
        self.stdout.write('Succesully created server %s\n' % server)
