# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class ExternalVaultAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address=None, secrets_engine_path=None, auth_method=None):  # noqa: E501
        """ExternalVaultAllOf - a model defined in OpenAPI

        :param address: The address of this ExternalVaultAllOf.  # noqa: E501
        :type address: str
        :param secrets_engine_path: The secrets_engine_path of this ExternalVaultAllOf.  # noqa: E501
        :type secrets_engine_path: str
        :param auth_method: The auth_method of this ExternalVaultAllOf.  # noqa: E501
        :type auth_method: str
        """
        self.openapi_types = {
            'address': str,
            'secrets_engine_path': str,
            'auth_method': str
        }

        self.attribute_map = {
            'address': 'address',
            'secrets_engine_path': 'secrets_engine_path',
            'auth_method': 'auth_method'
        }

        self._address = address
        self._secrets_engine_path = secrets_engine_path
        self._auth_method = auth_method

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalVaultAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalVault_allOf of this ExternalVaultAllOf.  # noqa: E501
        :rtype: ExternalVaultAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this ExternalVaultAllOf.

        The URL of your Hashicorp Vault instance  # noqa: E501

        :return: The address of this ExternalVaultAllOf.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ExternalVaultAllOf.

        The URL of your Hashicorp Vault instance  # noqa: E501

        :param address: The address of this ExternalVaultAllOf.
        :type address: str
        """

        self._address = address

    @property
    def secrets_engine_path(self):
        """Gets the secrets_engine_path of this ExternalVaultAllOf.

        Vault secrets engine path  # noqa: E501

        :return: The secrets_engine_path of this ExternalVaultAllOf.
        :rtype: str
        """
        return self._secrets_engine_path

    @secrets_engine_path.setter
    def secrets_engine_path(self, secrets_engine_path):
        """Sets the secrets_engine_path of this ExternalVaultAllOf.

        Vault secrets engine path  # noqa: E501

        :param secrets_engine_path: The secrets_engine_path of this ExternalVaultAllOf.
        :type secrets_engine_path: str
        """

        self._secrets_engine_path = secrets_engine_path

    @property
    def auth_method(self):
        """Gets the auth_method of this ExternalVaultAllOf.


        :return: The auth_method of this ExternalVaultAllOf.
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this ExternalVaultAllOf.


        :param auth_method: The auth_method of this ExternalVaultAllOf.
        :type auth_method: str
        """
        allowed_values = ["AppRole", "Token"]  # noqa: E501
        if auth_method not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_method` ({0}), must be one of {1}"
                .format(auth_method, allowed_values)
            )

        self._auth_method = auth_method
