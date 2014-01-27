Opendevelop Private Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can easily build a private installation of Opendevelop and give your
users the chance to run code in the cloud.

Opendevelop is a Django project which dispatches the requests to the docker
servers. So an opendevelop installation should have one web server and multiple
docker servers.

Install
=======

At first you should clone the Opendevelop public repository.

.. code-block:: bash

    git clone git@bitbucket.org:sourcelair/opendevelop.git


Next thing to do is run the install script as a root user from the root directory of opendevelop.

.. code-block:: bash

    sudo python installer.py


Starting the service
---------
In order to get OpenDevelop up and running you need to start the *Celery* and the *Django server* from the
command line, from within the manage.py directory, in two different Bash sessions.

.. code-block:: bash

    ./manage.py runserver


.. code-block:: bash

    ./manage.py celeryd
DockerServer
------------

Management
===========

Opendevelop makes use of the
`Django Admin Panel <https://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_
. So the addition of a new App, a new DockerServer or a new Image is done through
the admin panel.

Adding an App
-------------
.. image:: images/add-app.png
    :target: _images/add-image.png
    :scale: 20 %

Adding a DockerServer
----------------------

Adding an Image
----------------
