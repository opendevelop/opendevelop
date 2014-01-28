Opendevelop Private Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can easily build a private installation of Opendevelop and give your
users the chance to run code in the cloud.

Opendevelop is a Django project which dispatches the requests to the docker
servers. So an opendevelop installation should have one web server and multiple
docker servers.

Install
=======

OpenDevelop is being developed using Ubuntu and until it reaches a more stable state, the
documentation will assume you are installing it on an Ubuntu machine, preferably Ubuntu 13.10 or
greater.

At first you should clone the Opendevelop public repository.

.. code-block:: bash

    git clone git@github.com:sourceLair/opendevelop.git


Before running the installer make sure you have *rabbitmq-server* install. If you do not have it installed
you can run

.. code-block:: bash

    sudo apt-get install rabbitmq-server

on your terminal to install it.

Next thing to do is run the install script as a root user from the root directory of opendevelop.

.. code-block:: bash

    sudo python install/installer.py

Last thing is to create the OpenDevelop models into the database. To do that you have to run the following
two commands, from within the manage.py directory. 

.. code-block:: bash

    ./manage.py syncdb
    ./manage.py migrate


Starting the service
---------
In order to get OpenDevelop up and running you need to start the *Celery* and the *Django server* from the
command line, from within the manage.py directory, in two different Bash sessions.

.. code-block:: bash

    ./manage.py runserver


.. code-block:: bash

    ./manage.py celeryd
