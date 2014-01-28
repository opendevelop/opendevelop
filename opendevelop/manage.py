#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    venv_path = '/etc/opendevelop/venv'
    if (os.path.exists(venv_path)):
        activate_this_file = os.path.join(venv_path, 'bin/activate_this.py')
        execfile(activate_this_file, dict(__file__=activate_this_file))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opendevelop.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
