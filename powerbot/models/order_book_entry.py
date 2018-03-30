# coding: utf-8

"""
    Powerbot Server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderBookEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'order_id': 'int',
        'order_entry_time': 'datetime',
        'price': 'float',
        'quantity': 'float'
    }

    attribute_map = {
        'order_id': 'order_id',
        'order_entry_time': 'order_entry_time',
        'price': 'price',
        'quantity': 'quantity'
    }

    def __init__(self, order_id=None, order_entry_time=None, price=None, quantity=None):  # noqa: E501
        """OrderBookEntry - a model defined in Swagger"""  # noqa: E501

        self._order_id = None
        self._order_entry_time = None
        self._price = None
        self._quantity = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if order_entry_time is not None:
            self.order_entry_time = order_entry_time
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    @property
    def order_id(self):
        """Gets the order_id of this OrderBookEntry.  # noqa: E501


        :return: The order_id of this OrderBookEntry.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderBookEntry.


        :param order_id: The order_id of this OrderBookEntry.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def order_entry_time(self):
        """Gets the order_entry_time of this OrderBookEntry.  # noqa: E501


        :return: The order_entry_time of this OrderBookEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._order_entry_time

    @order_entry_time.setter
    def order_entry_time(self, order_entry_time):
        """Sets the order_entry_time of this OrderBookEntry.


        :param order_entry_time: The order_entry_time of this OrderBookEntry.  # noqa: E501
        :type: datetime
        """

        self._order_entry_time = order_entry_time

    @property
    def price(self):
        """Gets the price of this OrderBookEntry.  # noqa: E501


        :return: The price of this OrderBookEntry.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderBookEntry.


        :param price: The price of this OrderBookEntry.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this OrderBookEntry.  # noqa: E501


        :return: The quantity of this OrderBookEntry.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderBookEntry.


        :param quantity: The quantity of this OrderBookEntry.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderBookEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other