# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.temperature import Temperature  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTemperaturaController(BaseTestCase):
    """TemperaturaController integration test stubs"""

    def test_delete_temperature(self):
        """Test case for delete_temperature

        Eliminación de datos de temperatura.
        """
        query_string = [('id_temperature', 56)]
        response = self.client.open(
            '/temperature',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_temperature(self):
        """Test case for get_temperature

        Devuelve todos los datos relacionados con la temperatura.
        """
        query_string = [('date', 'date_example')]
        response = self.client.open(
            '/temperature',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_temperature(self):
        """Test case for post_temperature

        Registra un nuevo dato de temperatura.
        """
        temperature = Temperature()
        response = self.client.open(
            '/temperature',
            method='POST',
            data=json.dumps(temperature),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_temperature(self):
        """Test case for put_temperature

        Modifica un dato de temperatura previamente registrado
        """
        temperature = Temperature()
        response = self.client.open(
            '/temperature',
            method='PUT',
            data=json.dumps(temperature),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
