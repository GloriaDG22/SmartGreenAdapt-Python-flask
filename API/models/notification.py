# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ..models.base_model_ import Model
from .. import util


class Notification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id_notification=None, amount=None, date=None):  # noqa: E501
        """Notification - a model defined in OpenAPI

        :param id_notification: The id_notification of this Notification.  # noqa: E501
        :type id_notification: int
        :param amount: The amount of this Notification.  # noqa: E501
        :type amount: float
        :param date: The date of this Notification.  # noqa: E501
        :type date: str
        """
        self.openapi_types = {
            'id_notification': int,
            'amount': float,
            'date': str
        }

        self.attribute_map = {
            'id_notification': 'idNotification',
            'amount': 'amount',
            'date': 'date'
        }

        self._id_notification = id_notification
        self._amount = amount
        self._date = date

    @classmethod
    def from_dict(cls, dikt) -> 'Notification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Notification of this Notification.  # noqa: E501
        :rtype: Notification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_notification(self):
        """Gets the id_notification of this Notification.


        :return: The id_notification of this Notification.
        :rtype: int
        """
        return self._id_notification

    @id_notification.setter
    def id_notification(self, id_notification):
        """Sets the id_notification of this Notification.


        :param id_notification: The id_notification of this Notification.
        :type id_notification: int
        """

        self._id_notification = id_notification

    @property
    def amount(self):
        """Gets the amount of this Notification.


        :return: The amount of this Notification.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Notification.


        :param amount: The amount of this Notification.
        :type amount: float
        """

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this Notification.


        :return: The date of this Notification.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Notification.


        :param date: The date of this Notification.
        :type date: str
        """

        self._date = date
