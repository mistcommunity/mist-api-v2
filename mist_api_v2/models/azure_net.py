# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AzureNet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, network=None):  # noqa: E501
        """AzureNet - a model defined in OpenAPI

        :param network: The network of this AzureNet.  # noqa: E501
        :type network: str
        """
        self.openapi_types = {
            'network': str
        }

        self.attribute_map = {
            'network': 'network'
        }

        self._network = network

    @classmethod
    def from_dict(cls, dikt) -> 'AzureNet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AzureNet of this AzureNet.  # noqa: E501
        :rtype: AzureNet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network(self):
        """Gets the network of this AzureNet.

        A new or existing network If not provided a `mist-resource_group-location` network will be used.  # noqa: E501

        :return: The network of this AzureNet.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this AzureNet.

        A new or existing network If not provided a `mist-resource_group-location` network will be used.  # noqa: E501

        :param network: The network of this AzureNet.
        :type network: str
        """

        self._network = network
