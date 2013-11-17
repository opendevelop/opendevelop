"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson as json
import models_factory as mf
import base64

APP = mf.AppFactory()
C_ID = APP.client_id
C_SECRET = APP.client_secret
hashed = base64.standard_b64encode("%s:%s" % (C_ID, C_SECRET))
value = "Basic " + hashed
headers = {"HTTP_AUTHORIZATION": value}

class SandBoxApiTest(TestCase):

    def test_get_sandbox(self):
        response = self.client.get("/api/sandbox/1",**headers)
        print "get_sandbox id =  " +  response.content

    def test_get_sandboxes(self):
        response = self.client.post("/api/sandbox/")
        print response.content

    def test_create_sandbox(self):
        response = self.client.post("/api/sandbox")
        info = json.loads(response.content)
        self.assertTrue(isinstance(info['sandbox_id'], int))
