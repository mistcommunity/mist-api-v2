# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class OneOffScheduleEntry(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datetime=None):  # noqa: E501
        """OneOffScheduleEntry - a model defined in OpenAPI

        :param datetime: The datetime of this OneOffScheduleEntry.  # noqa: E501
        :type datetime: datetime
        """
        self.openapi_types = {
            'datetime': datetime
        }

        self.attribute_map = {
            'datetime': 'datetime'
        }

        self._datetime = datetime

    @classmethod
    def from_dict(cls, dikt) -> 'OneOffScheduleEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OneOffScheduleEntry of this OneOffScheduleEntry.  # noqa: E501
        :rtype: OneOffScheduleEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datetime(self):
        """Gets the datetime of this OneOffScheduleEntry.

        When schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :return: The datetime of this OneOffScheduleEntry.
        :rtype: datetime
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this OneOffScheduleEntry.

        When schedule should run, e.g 2021-09-22T18:19:28Z  # noqa: E501

        :param datetime: The datetime of this OneOffScheduleEntry.
        :type datetime: datetime
        """
        if datetime is None:
            raise ValueError("Invalid value for `datetime`, must not be `None`")  # noqa: E501

        self._datetime = datetime
