# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ScriptToRunAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, action_type=None, script_type=None):  # noqa: E501
        """ScriptToRunAllOf - a model defined in OpenAPI

        :param action_type: The action_type of this ScriptToRunAllOf.  # noqa: E501
        :type action_type: str
        :param script_type: The script_type of this ScriptToRunAllOf.  # noqa: E501
        :type script_type: str
        """
        self.openapi_types = {
            'action_type': str,
            'script_type': str
        }

        self.attribute_map = {
            'action_type': 'action_type',
            'script_type': 'script_type'
        }

        self._action_type = action_type
        self._script_type = script_type

    @classmethod
    def from_dict(cls, dikt) -> 'ScriptToRunAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScriptToRun_allOf of this ScriptToRunAllOf.  # noqa: E501
        :rtype: ScriptToRunAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action_type(self):
        """Gets the action_type of this ScriptToRunAllOf.


        :return: The action_type of this ScriptToRunAllOf.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ScriptToRunAllOf.


        :param action_type: The action_type of this ScriptToRunAllOf.
        :type action_type: str
        """
        allowed_values = ["run_script"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def script_type(self):
        """Gets the script_type of this ScriptToRunAllOf.


        :return: The script_type of this ScriptToRunAllOf.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this ScriptToRunAllOf.


        :param script_type: The script_type of this ScriptToRunAllOf.
        :type script_type: str
        """
        allowed_values = ["inline", "existing"]  # noqa: E501
        if script_type not in allowed_values:
            raise ValueError(
                "Invalid value for `script_type` ({0}), must be one of {1}"
                .format(script_type, allowed_values)
            )

        self._script_type = script_type
