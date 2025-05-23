# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class TaggingSelector(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, include=None):  # noqa: E501
        """TaggingSelector - a model defined in OpenAPI

        :param type: The type of this TaggingSelector.  # noqa: E501
        :type type: str
        :param include: The include of this TaggingSelector.  # noqa: E501
        :type include: List[str]
        """
        self.openapi_types = {
            'type': str,
            'include': List[str]
        }

        self.attribute_map = {
            'type': 'type',
            'include': 'include'
        }

        self._type = type
        self._include = include

    @classmethod
    def from_dict(cls, dikt) -> 'TaggingSelector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TaggingSelector of this TaggingSelector.  # noqa: E501
        :rtype: TaggingSelector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this TaggingSelector.

        tag type  # noqa: E501

        :return: The type of this TaggingSelector.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaggingSelector.

        tag type  # noqa: E501

        :param type: The type of this TaggingSelector.
        :type type: str
        """
        allowed_values = ["tags"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def include(self):
        """Gets the include of this TaggingSelector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :return: The include of this TaggingSelector.
        :rtype: List[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this TaggingSelector.

        a list of tags in case type is \"tags\"  # noqa: E501

        :param include: The include of this TaggingSelector.
        :type include: List[str]
        """

        self._include = include
