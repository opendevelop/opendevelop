"""
This Python script should handle the installing
of OpenDevelop.
  - The installer should be run as root
"""

from getpass import getuser
from sys import exit
from sys import stderr

def die(error, exit_code=1):
    """
    Writes error to `stderr` pipe and exits with the
    given exit code
    """
    error += '\n'
    stderr.write(error)
    exit(exit_code)

USER = getuser()
if (not USER == 'root'):
    die('The installer has to be run as root.')
