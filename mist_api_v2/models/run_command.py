# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class RunCommand(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, script_type=None, command=None):  # noqa: E501
        """RunCommand - a model defined in OpenAPI

        :param script_type: The script_type of this RunCommand.  # noqa: E501
        :type script_type: str
        :param command: The command of this RunCommand.  # noqa: E501
        :type command: str
        """
        self.openapi_types = {
            'script_type': str,
            'command': str
        }

        self.attribute_map = {
            'script_type': 'script_type',
            'command': 'command'
        }

        self._script_type = script_type
        self._command = command

    @classmethod
    def from_dict(cls, dikt) -> 'RunCommand':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RunCommand of this RunCommand.  # noqa: E501
        :rtype: RunCommand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def script_type(self):
        """Gets the script_type of this RunCommand.


        :return: The script_type of this RunCommand.
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this RunCommand.


        :param script_type: The script_type of this RunCommand.
        :type script_type: str
        """
        allowed_values = ["inline"]  # noqa: E501
        if script_type not in allowed_values:
            raise ValueError(
                "Invalid value for `script_type` ({0}), must be one of {1}"
                .format(script_type, allowed_values)
            )

        self._script_type = script_type

    @property
    def command(self):
        """Gets the command of this RunCommand.

        Command that is about to run  # noqa: E501

        :return: The command of this RunCommand.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this RunCommand.

        Command that is about to run  # noqa: E501

        :param command: The command of this RunCommand.
        :type command: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command
