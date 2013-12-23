"""
This Python script should handle the installing
of OpenDevelop.
  - The installer should be run as root
"""

from getpass import getuser
from os import environ
from os import mkdir
from os.path import exists
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

# Add current user and sudo user (if exists) to opendevelop group
OPENDEVELOP_USERS = [USER]
if ('SUDO_USER' in environ):
    OPENDEVELOP_USERS.append(environ['SUDO_USER'])
for od_user in OPENDEVELOP_USERS:
    print 'Adding user %s to group %s' % (od_user, USER_NAME)
    args = ['usermod', '-aG', USER_NAME, od_user]
    result = call(args, stdout=PIPE, stderr=PIPE)
    if (result):
        die('  Cannot add user %s to opendevelop group. Exiting.' % od_user)
    print '  Okay.'

# Create application directory
APP_DIR = '/etc/%s' % USER_NAME
print 'Creating application directory...'
if (exists(APP_DIR)):
    print '  Application directory already exists. Skipping...'
else:
    mkdir(APP_DIR)
    print '  Okay.'

# Set proper ownership and permissions for the directory
APP_OWNER = '%s:%s' % (USER_NAME, USER_NAME)
print 'Setting proper ownership and permissions for the directory...'
call(['chown', APP_OWNER, APP_DIR], stdout=PIPE, stderr=PIPE)
call(['chmod', '775', APP_DIR], stdout=PIPE, stderr=PIPE)
print '  Okay.'

# Exit
print 'Ready to go.'
