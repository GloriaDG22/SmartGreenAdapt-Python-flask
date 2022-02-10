# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.humidity import Humidity  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHumedadController(BaseTestCase):
    """HumedadController integration test stubs"""

    def test_delete_humidity(self):
        """Test case for delete_humidity

        Eliminación de datos de humedad.
        """
        query_string = [('id_humidity', 56)]
        response = self.client.open(
            '/humidity',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_humidity(self):
        """Test case for get_humidity

        Devuelve todos los datos relacionados con la humedad.
        """
        query_string = [('date', 'date_example')]
        response = self.client.open(
            '/humidity',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_humidity(self):
        """Test case for post_humidity

        Registra un nuevo dato de humedad.
        """
        humidity = Humidity()
        response = self.client.open(
            '/humidity',
            method='POST',
            data=json.dumps(humidity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_humidity(self):
        """Test case for put_humidity

        Modifica un dato de humedad previamente registrado
        """
        humidity = Humidity()
        response = self.client.open(
            '/humidity',
            method='PUT',
            data=json.dumps(humidity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
