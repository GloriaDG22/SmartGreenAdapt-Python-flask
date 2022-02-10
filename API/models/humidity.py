# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Humidity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_humidity=None, amount=None, date=None):  # noqa: E501
        """Humidity - a model defined in OpenAPI

        :param id_humidity: The id_humidity of this Humidity.  # noqa: E501
        :type id_humidity: int
        :param amount: The amount of this Humidity.  # noqa: E501
        :type amount: float
        :param date: The date of this Humidity.  # noqa: E501
        :type date: str
        """
        self.openapi_types = {
            'id_humidity': int,
            'amount': float,
            'date': str
        }

        self.attribute_map = {
            'id_humidity': 'idHumidity',
            'amount': 'amount',
            'date': 'date'
        }

        self._id_humidity = id_humidity
        self._amount = amount
        self._date = date

    @classmethod
    def from_dict(cls, dikt) -> 'Humidity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Humidity of this Humidity.  # noqa: E501
        :rtype: Humidity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_humidity(self):
        """Gets the id_humidity of this Humidity.


        :return: The id_humidity of this Humidity.
        :rtype: int
        """
        return self._id_humidity

    @id_humidity.setter
    def id_humidity(self, id_humidity):
        """Sets the id_humidity of this Humidity.


        :param id_humidity: The id_humidity of this Humidity.
        :type id_humidity: int
        """

        self._id_humidity = id_humidity

    @property
    def amount(self):
        """Gets the amount of this Humidity.


        :return: The amount of this Humidity.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Humidity.


        :param amount: The amount of this Humidity.
        :type amount: float
        """

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this Humidity.


        :return: The date of this Humidity.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Humidity.


        :param date: The date of this Humidity.
        :type date: str
        """

        self._date = date