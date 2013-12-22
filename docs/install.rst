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

Webserver
---------

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
