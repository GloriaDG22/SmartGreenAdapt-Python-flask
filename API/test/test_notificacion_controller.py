# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.notification import Notification  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNotificacionController(BaseTestCase):
    """NotificacionController integration test stubs"""

    def test_get_notification(self):
        """Test case for get_notification

        Devuelve todos los datos relacionados con notificaciones.
        """
        query_string = [('date', 'date_example')]
        response = self.client.open(
            '/notification',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_notification(self):
        """Test case for post_notification

        Registra una nueva notificación.
        """
        notification = Notification()
        response = self.client.open(
            '/notification',
            method='POST',
            data=json.dumps(notification),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
