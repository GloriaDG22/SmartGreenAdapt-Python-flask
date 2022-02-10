# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.air_quality import AirQuality  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCalidadDelAireController(BaseTestCase):
    """CalidadDelAireController integration test stubs"""

    def test_delete_air_quality(self):
        """Test case for delete_air_quality

        Eliminación de datos de la calidad del aire.
        """
        query_string = [('id_air_quality', 56)]
        response = self.client.open(
            '/airquality',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_air_quality(self):
        """Test case for get_air_quality

        Devuelve todos los datos relacionados con la calidad del aire.
        """
        query_string = [('date', 'date_example')]
        response = self.client.open(
            '/airquality',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_air_quality(self):
        """Test case for post_air_quality

        Registra un nuevo dato de calidad del aire.
        """
        air_quality = AirQuality()
        response = self.client.open(
            '/airquality',
            method='POST',
            data=json.dumps(air_quality),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_air_quality(self):
        """Test case for put_air_quality

        Modifica un dato de calidad del aire previamente registrado
        """
        air_quality = AirQuality()
        response = self.client.open(
            '/airquality',
            method='PUT',
            data=json.dumps(air_quality),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
