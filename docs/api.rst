Opendevelop API
^^^^^^^^^^^^^^^


RESTful API
===========

Opendevelop's end user has at his disposal an asynchronous HTTP REST API to use
and easily run code.

Authentication
---------------

In order to make API calls the user will need to be authenticated according to
OAuth protocol. So every request must include a Basic OAuth HTTP header
that includes the id and the secret key of the App.

.. code-block:: python

    {'HTTP_AUTHORIZATION' : "Basic " + base64("<id>:<secret>")}


API calls
=========

Sandboxes
---------
+------------+------------------------------+----------------------------------+
| Verb       | URI                          | Description                      |
+============+==============================+==================================+
| **GET**    | ``/api/sandbox``             | List all sandboxes associated    |
|            |                              | with the given App               |
+------------+------------------------------+----------------------------------+
| **GET**    | ``/api/sandbox/sandbox_id``  | Show information about a specific|
|            |                              | App                              |
+------------+------------------------------+----------------------------------+
| **POST**   | ``/api/sandbox``             | Create a new sandbox and run the |
|            |                              | given code inside                |
+------------+------------------------------+----------------------------------+

**List Sandboxes**

**Show Sandbox**

**Create Sandbox**

Images
------
