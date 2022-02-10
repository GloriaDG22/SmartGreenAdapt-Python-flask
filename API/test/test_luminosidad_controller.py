# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.luminosity import Luminosity  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLuminosidadController(BaseTestCase):
    """LuminosidadController integration test stubs"""

    def test_delete_luminosity(self):
        """Test case for delete_luminosity

        Eliminación de datos de luminosidad.
        """
        query_string = [('id_luminosity', 56)]
        response = self.client.open(
            '/luminosity',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_luminosity(self):
        """Test case for get_luminosity

        Devuelve todos los datos relacionados con la luminosidad.
        """
        query_string = [('date', 'date_example')]
        response = self.client.open(
            '/luminosity',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_luminosity(self):
        """Test case for post_luminosity

        Registra un nuevo dato de luminosidad.
        """
        luminosity = Luminosity()
        response = self.client.open(
            '/luminosity',
            method='POST',
            data=json.dumps(luminosity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_luminosity(self):
        """Test case for put_luminosity

        Modifica un dato de luminosidad previamente registrado
        """
        luminosity = Luminosity()
        response = self.client.open(
            '/luminosity',
            method='PUT',
            data=json.dumps(luminosity),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
