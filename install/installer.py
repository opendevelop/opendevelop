"""
This Python script should handle the installing
of OpenDevelop.
  - The installer should be run as root
"""

from getpass import getuser
from subprocess import call
from subprocess import PIPE
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

# Check if script is run by root user
USER = getuser()
if (not USER == 'root'):
    die('The installer has to be run as root.')

# Create opendevelop user and group
USER_NAME = 'opendevelop'
print 'Creating user and group %s...' % USER_NAME
if (call(['id', USER_NAME], stdout=PIPE, stderr=PIPE)):
    if (call(['useradd', USER_NAME, '-U'])):
        die('Could not create user %s' % USER_NAME)
    print '  Okay.'
else:
    print '  It seems like the user already exists. Skipping...'
