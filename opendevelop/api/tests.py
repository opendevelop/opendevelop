"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson as json
import models_factory as mf
from sandboxes import models_factory as smf
from images import models_factory as imf
import base64
import models
from mock import patch


class SandBoxApiTest(TestCase):

    def setUp(self):
        self.app = mf.AppFactory()
        C_ID = self.app.client_id
        C_SECRET = self.app.client_secret
        hashed = base64.standard_b64encode("%s:%s" % (C_ID, C_SECRET))
        value = "Basic " + hashed
        self.headers = {"HTTP_AUTHORIZATION": value}

    def test_unauthorized(self):
        response = self.client.get("/api/sandbox")
        self.assertEqual(response.status_code, 401)

    def test_wrong_header(self):
        response = self.client.get("/api/sandbox", HTTP_AUTHORIZATION="wrong")
        self.assertEqual(response.status_code, 400)

    def test_no_app_found(self):
        C_ID = "                    "
        C_SECRET = "                                        "
        hashed = base64.standard_b64encode("%s:%s" % (C_ID, C_SECRET))
        value = "Basic " + hashed
        header = {"HTTP_AUTHORIZATION": value}
        response = self.client.get("/api/sandbox/", **header)
        self.assertEqual(response.status_code, 400)

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

    def test_create_sandbox_invalid_json(self):
        response = self.client.post("/api/sandbox/", **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_create_sandbox_image_missing(self):
        req = {"cmd": "foo"}
        a = json.dumps(req)
        response = self.client.post("/api/sandbox/", req, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_create_sandbox_cmd_missing(self):
        req = {"image_id": "foo"}
        response = self.client.post("/api/sandbox/", req, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_create_sandbox_wrong_image(self):
        req = {"image_id": "foo", "cmd": "bar"}
        response = self.client.post("/api/sandbox/", req, **self.headers)
        self.assertEqual(response.status_code, 404)

    def test_create_sandbox(self):
        with patch("sandboxes.logic.create") as f:
            f.return_value = 100
            image = imf.ImageFactory()
            req = {"image_id": image.id, "cmd": "bar"}
            response = self.client.post("/api/sandbox/", req,  **self.headers)
            self.assertEqual(response.status_code, 200)
