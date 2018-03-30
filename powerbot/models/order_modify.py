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


class OrderModify(object):
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
        'action': 'str',
        'validity_res': 'str',
        'validity_date': 'datetime',
        'type': 'str',
        'txt': 'str',
        'ordr_exe_restriction': 'str',
        'quantity': 'float',
        'display_qty': 'int',
        'price': 'float',
        'cl_ordr_id': 'str',
        'ppd': 'int'
    }

    attribute_map = {
        'action': 'action',
        'validity_res': 'validityRes',
        'validity_date': 'validityDate',
        'type': 'type',
        'txt': 'txt',
        'ordr_exe_restriction': 'ordrExeRestriction',
        'quantity': 'quantity',
        'display_qty': 'displayQty',
        'price': 'price',
        'cl_ordr_id': 'clOrdrId',
        'ppd': 'ppd'
    }

    def __init__(self, action=None, validity_res=None, validity_date=None, type=None, txt=None, ordr_exe_restriction=None, quantity=None, display_qty=None, price=None, cl_ordr_id=None, ppd=None):  # noqa: E501
        """OrderModify - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._validity_res = None
        self._validity_date = None
        self._type = None
        self._txt = None
        self._ordr_exe_restriction = None
        self._quantity = None
        self._display_qty = None
        self._price = None
        self._cl_ordr_id = None
        self._ppd = None
        self.discriminator = None

        self.action = action
        if validity_res is not None:
            self.validity_res = validity_res
        if validity_date is not None:
            self.validity_date = validity_date
        if type is not None:
            self.type = type
        if txt is not None:
            self.txt = txt
        if ordr_exe_restriction is not None:
            self.ordr_exe_restriction = ordr_exe_restriction
        if quantity is not None:
            self.quantity = quantity
        if display_qty is not None:
            self.display_qty = display_qty
        if price is not None:
            self.price = price
        if cl_ordr_id is not None:
            self.cl_ordr_id = cl_ordr_id
        if ppd is not None:
            self.ppd = ppd

    @property
    def action(self):
        """Gets the action of this OrderModify.  # noqa: E501


        :return: The action of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this OrderModify.


        :param action: The action of this OrderModify.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTI", "DEAC", "MODI", "DELE"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def validity_res(self):
        """Gets the validity_res of this OrderModify.  # noqa: E501


        :return: The validity_res of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._validity_res

    @validity_res.setter
    def validity_res(self, validity_res):
        """Sets the validity_res of this OrderModify.


        :param validity_res: The validity_res of this OrderModify.  # noqa: E501
        :type: str
        """
        allowed_values = ["GFS", "GTD", "NON"]  # noqa: E501
        if validity_res not in allowed_values:
            raise ValueError(
                "Invalid value for `validity_res` ({0}), must be one of {1}"  # noqa: E501
                .format(validity_res, allowed_values)
            )

        self._validity_res = validity_res

    @property
    def validity_date(self):
        """Gets the validity_date of this OrderModify.  # noqa: E501


        :return: The validity_date of this OrderModify.  # noqa: E501
        :rtype: datetime
        """
        return self._validity_date

    @validity_date.setter
    def validity_date(self, validity_date):
        """Sets the validity_date of this OrderModify.


        :param validity_date: The validity_date of this OrderModify.  # noqa: E501
        :type: datetime
        """

        self._validity_date = validity_date

    @property
    def type(self):
        """Gets the type of this OrderModify.  # noqa: E501


        :return: The type of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrderModify.


        :param type: The type of this OrderModify.  # noqa: E501
        :type: str
        """
        allowed_values = ["B", "O", "I", "L", "S", "H", "C", "N", "E"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def txt(self):
        """Gets the txt of this OrderModify.  # noqa: E501


        :return: The txt of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._txt

    @txt.setter
    def txt(self, txt):
        """Sets the txt of this OrderModify.


        :param txt: The txt of this OrderModify.  # noqa: E501
        :type: str
        """
        if txt is not None and len(txt) > 250:
            raise ValueError("Invalid value for `txt`, length must be less than or equal to `250`")  # noqa: E501

        self._txt = txt

    @property
    def ordr_exe_restriction(self):
        """Gets the ordr_exe_restriction of this OrderModify.  # noqa: E501


        :return: The ordr_exe_restriction of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._ordr_exe_restriction

    @ordr_exe_restriction.setter
    def ordr_exe_restriction(self, ordr_exe_restriction):
        """Sets the ordr_exe_restriction of this OrderModify.


        :param ordr_exe_restriction: The ordr_exe_restriction of this OrderModify.  # noqa: E501
        :type: str
        """
        allowed_values = ["FOK", "IOC", "NON", "AON", "AU"]  # noqa: E501
        if ordr_exe_restriction not in allowed_values:
            raise ValueError(
                "Invalid value for `ordr_exe_restriction` ({0}), must be one of {1}"  # noqa: E501
                .format(ordr_exe_restriction, allowed_values)
            )

        self._ordr_exe_restriction = ordr_exe_restriction

    @property
    def quantity(self):
        """Gets the quantity of this OrderModify.  # noqa: E501


        :return: The quantity of this OrderModify.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderModify.


        :param quantity: The quantity of this OrderModify.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def display_qty(self):
        """Gets the display_qty of this OrderModify.  # noqa: E501


        :return: The display_qty of this OrderModify.  # noqa: E501
        :rtype: int
        """
        return self._display_qty

    @display_qty.setter
    def display_qty(self, display_qty):
        """Sets the display_qty of this OrderModify.


        :param display_qty: The display_qty of this OrderModify.  # noqa: E501
        :type: int
        """

        self._display_qty = display_qty

    @property
    def price(self):
        """Gets the price of this OrderModify.  # noqa: E501


        :return: The price of this OrderModify.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OrderModify.


        :param price: The price of this OrderModify.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def cl_ordr_id(self):
        """Gets the cl_ordr_id of this OrderModify.  # noqa: E501


        :return: The cl_ordr_id of this OrderModify.  # noqa: E501
        :rtype: str
        """
        return self._cl_ordr_id

    @cl_ordr_id.setter
    def cl_ordr_id(self, cl_ordr_id):
        """Sets the cl_ordr_id of this OrderModify.


        :param cl_ordr_id: The cl_ordr_id of this OrderModify.  # noqa: E501
        :type: str
        """
        if cl_ordr_id is not None and len(cl_ordr_id) > 40:
            raise ValueError("Invalid value for `cl_ordr_id`, length must be less than or equal to `40`")  # noqa: E501

        self._cl_ordr_id = cl_ordr_id

    @property
    def ppd(self):
        """Gets the ppd of this OrderModify.  # noqa: E501


        :return: The ppd of this OrderModify.  # noqa: E501
        :rtype: int
        """
        return self._ppd

    @ppd.setter
    def ppd(self, ppd):
        """Sets the ppd of this OrderModify.


        :param ppd: The ppd of this OrderModify.  # noqa: E501
        :type: int
        """

        self._ppd = ppd

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
        if not isinstance(other, OrderModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
