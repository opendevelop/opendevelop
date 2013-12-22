Opendevelop Basic Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sandbox
=======

The core of the opendevelop project is the sandbox. A sandbox is a linux
container created with `docker <https://www.docker.io/>`_. In this container the
end user can execute any kind of code in a secure and isolated way.

App
===

Every Sandbox that is created has to be associated with a specific App. An
opendevelop App is a logical entities that many sandboxes can be associated
with. Every App has an id and a secret key used for Oauth authentication in
every API call.

Opendevelop User
=================

An opendevelop App belongs to a user. Every user can have multiple Apps
associated with him.

Image
=====

Image is the logical entity that contains information about the image that
runs in the linux containers where used by the Sandboxes. The user can choose
and executed their code in images provided by Opendevelop or create their own
custom image so that running code with opendevelop feels really like home.

DockerServer
============

The Opendevelop's architecture is designed in such a way so that it can easily
scale up in a destributed way. So a DockerServer is a server where the Sandboxes
are created and the code is executed. This way the webserver that serves
Opendevelop chooses where to dispatch the incoming requests for sandbox
creations.

