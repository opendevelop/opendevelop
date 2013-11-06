"""
This module should handle the `run` command for manage.py
Run should read settings from /etc/opendevelop/settings.yaml
and run the service according to these settings
"""

from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.runserver import Command as Runserver
import sys

class Command(BaseCommand):
    """
    This class defines the `run` command for manage.py
    """

    help = 'Starts the opendevelop server'
    def handle(self, *args, **options):
        """
        This function prepares the options for running the service
        and if needed delegates the whole procedure to `runserver`
        """
        runserver = Runserver()
        runserver.stdout = sys.stdout
        runserver.handle('0.0.0.0:8000', *args, **options)
