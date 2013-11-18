"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson as json
import models_factory as mf
from  sandboxes import models_factory as smf
import base64
import models


class SandBoxApiTest(TestCase):

    def setUp(self):
        self.app = mf.AppFactory()
        C_ID = self.app.client_id
        C_SECRET = self.app.client_secret
        hashed = base64.standard_b64encode("%s:%s" % (C_ID, C_SECRET))
        value = "Basic " + hashed
        self.headers = {"HTTP_AUTHORIZATION": value}

    def test_get_sandboxes_empty(self):
        response = self.client.get("/api/sandbox/", **self.headers)
        self.assertEqual(response.content, "{\"sandboxes\": []}")

    def test_get_sandbox_not_found(self):
        response = self.client.get("/api/sandbox/1123", **self.headers)
        self.assertEqual(response.status_code, 404)

    def test_get_sandbox(self):
        sbx = smf.SandboxFactory(owner_app=self.app)
        response = self.client.get("/api/sandbox/"+str(sbx.id), **self.headers)
        self.assertEqual(response.status_code, 200)

    '''
    def test_create_sandbox(self):
        response = self.client.post("/api/sandbox")
        info = json.loads(response.content)
        self.assertTrue(isinstance(info['sandbox_id'], int))
    '''
