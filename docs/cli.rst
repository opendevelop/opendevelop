Opendevelop Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenDevelop comes bundled with a command line interface that helps you administer your
OpenDevelop instance. To get more information about every command, you can run

.. code-block:: bash

    ./manage.py <command> -h


Add a Docker server
===================
In order to add a new Docker server to OpenDevelop, you have to run the following command:

.. code-block:: bash

    ./manage.py server-create --name=name_of_your_server --url=docker_api_url --buckets=buckets_directory


Add a new user
==============
In order to add a new OpenDevelop user, you have to run the following command 
(the `--organization` flag is optional and declares the new account as an organization 
account):

.. code-block:: bash

    ./manage.py user-create --username=sourcelair --email=opendevelop@soureclair.com --passwd=123 --organization


Add a new app
=============
To create a new OpenDevelop app, you have to run the following command, by supplying
the name of your app and the username of the owner

.. code-block:: bash

    ./manage.py app-create --name=myapp --username=user_that_owns_the_app


Add a new image
===============
To add a new OpenDevelop image you have to run the following command and supply
a name for your image, as well as a small description for it, its Docker image
counterpart and a docker index url

.. code-block:: bash

    ./manage.py image-create --name=my_image --description=what_my_image_does --url=docker_index_url --docker-image=docker_counterpart
