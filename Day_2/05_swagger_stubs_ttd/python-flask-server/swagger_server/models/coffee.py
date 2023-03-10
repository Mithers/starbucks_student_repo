# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Coffee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, coffee_name: str=None, milk: str=None):  # noqa: E501
        """Coffee - a model defined in Swagger

        :param coffee_name: The coffee_name of this Coffee.  # noqa: E501
        :type coffee_name: str
        :param milk: The milk of this Coffee.  # noqa: E501
        :type milk: str
        """
        self.swagger_types = {
            'coffee_name': str,
            'milk': str
        }

        self.attribute_map = {
            'coffee_name': 'coffee_name',
            'milk': 'milk'
        }

        self._coffee_name = coffee_name
        self._milk = milk

    @classmethod
    def from_dict(cls, dikt) -> 'Coffee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The coffee of this Coffee.  # noqa: E501
        :rtype: Coffee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coffee_name(self) -> str:
        """Gets the coffee_name of this Coffee.

        Name of drink  # noqa: E501

        :return: The coffee_name of this Coffee.
        :rtype: str
        """
        return self._coffee_name

    @coffee_name.setter
    def coffee_name(self, coffee_name: str):
        """Sets the coffee_name of this Coffee.

        Name of drink  # noqa: E501

        :param coffee_name: The coffee_name of this Coffee.
        :type coffee_name: str
        """

        self._coffee_name = coffee_name

    @property
    def milk(self) -> str:
        """Gets the milk of this Coffee.

        type of milk to use  # noqa: E501

        :return: The milk of this Coffee.
        :rtype: str
        """
        return self._milk

    @milk.setter
    def milk(self, milk: str):
        """Sets the milk of this Coffee.

        type of milk to use  # noqa: E501

        :param milk: The milk of this Coffee.
        :type milk: str
        """

        self._milk = milk
