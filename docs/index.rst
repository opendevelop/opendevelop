.. opendevelop documentation master file, created by
   sphinx-quickstart on Thu Dec 19 15:18:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to opendevelop's documentation!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overview
========

OpenDevelop is an open source platform dedicated on facilitating the procedure
of running code. It provides a state-of-the-art asynchronous REST API to allow
users run their code with a single HTTP request. OpenDevelop has been designed
and designated to be used by `sourceLair <https://www.sourcelair.com/>`_  as its
sole backend for any code-executing task.

However it is also opensource so that anyone can set up a private opendevelop
installation.

Opendevelop is based on the following technologies

* `Django <https://docs.djangoproject.com/>`_
* `Doker <https://www.docker.io/>`_
* `Celery <http://www.celeryproject.org/>`_

Contents
========

.. toctree::
    :maxdepth: 2
    :glob:

    concepts
    api
    clients
    install
