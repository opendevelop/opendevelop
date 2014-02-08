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

    {'Authorization' : "Basic " + base64("<id>:<secret>")}


API calls
=========

Sandboxes
---------
+----------+-------------------------------+-----------------------------------+
| Verb     | URI                           | Description                       |
+==========+===============================+===================================+
| **GET**  | ``/api/sandboxes``            | List all sandboxes associated     |
|          |                               | with the given App                |
+----------+-------------------------------+-----------------------------------+
| **GET**  | ``/api/sandboxes/sandbox_id`` | Show information about a specific |
|          |                               | App                               |
+----------+-------------------------------+-----------------------------------+
| **POST** | ``/api/sandboxes``            | Create a new sandbox and run the  |
|          |                               | given code inside                 |
+----------+-------------------------------+-----------------------------------+

**List Sandboxes**

Example request

.. code-block:: bash

    Request Url: http://opendevelop/api/sandboxes
    Request Method: GET
    Params: {}

Example response

.. code-block:: json

    {
    "sandboxes": [
        {
            "status": "terminated",
            "image": "my_image",
            "cmd": "[\"python test.py\"]",
            "return_code": 127,
            "logs": "sh: 0: Can't open start\n"
        },
        {
            "status": "running",
            "image": "my_image",
            "cmd": "[\"ls -a\"]",
            "return_code": null,
            "logs": null
        }
      ]
    }

**Show Sandbox**

Example request

.. code-block:: bash

    GET /api/sandboxes/1


Example response

.. code-block:: json

    {
    "status": "terminated",
    "image": "my_image",
    "cmd": "[\"python test.py\"]",
    "return_code": 0,
    "logs": "hello opendevelop!\n"
    }

**Create Sandbox**

Example request

.. code-block:: bash

    Request Url: http://opendevelop/api/sandboxes
    Request Method: POST
    Files: {
        "0": {
            "webkitRelativePath": "",
            "lastModifiedDate": "2013-12-22T22:27:47.000Z",
            "name": "test.py",
            "type": "text/x-python-script",
            "size": 46
           },
        "length": 1
    }
    Params: {
        "image": "my_image",
        "cmd": "[\"python test.py\"]"
        "timeout": "10"
    }

Timeout is an optional parameter that allows the user to specify the maximum 
time in seconds that the execution of the sandbox will last before it 
automatically gets killed.
 
Example response

.. code-block:: json

    a326efb1fe1f980a


Images
------

+------------+------------------------------+----------------------------------+
| Verb       | URI                          | Description                      |
+============+==============================+==================================+
| **GET**    | ``/api/images``              | List all available images to be  |
|            |                              | used for sandbox creation        |
+------------+------------------------------+----------------------------------+


Example request

.. code-block:: bash

    Request Url: http://opendevelop/api/images
    Request Method: GET
    Status Code: 200
    Params: {}

Example response

.. code-block:: json

    ["base"]
