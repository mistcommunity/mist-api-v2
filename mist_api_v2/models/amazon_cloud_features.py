# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class AmazonCloudFeatures(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compute=True, dns=False, container=False, objectstorage=None):  # noqa: E501
        """AmazonCloudFeatures - a model defined in OpenAPI

        :param compute: The compute of this AmazonCloudFeatures.  # noqa: E501
        :type compute: bool
        :param dns: The dns of this AmazonCloudFeatures.  # noqa: E501
        :type dns: bool
        :param container: The container of this AmazonCloudFeatures.  # noqa: E501
        :type container: bool
        :param objectstorage: The objectstorage of this AmazonCloudFeatures.  # noqa: E501
        :type objectstorage: bool
        """
        self.openapi_types = {
            'compute': bool,
            'dns': bool,
            'container': bool,
            'objectstorage': bool
        }

        self.attribute_map = {
            'compute': 'compute',
            'dns': 'dns',
            'container': 'container',
            'objectstorage': 'objectstorage'
        }

        self._compute = compute
        self._dns = dns
        self._container = container
        self._objectstorage = objectstorage

    @classmethod
    def from_dict(cls, dikt) -> 'AmazonCloudFeatures':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AmazonCloudFeatures of this AmazonCloudFeatures.  # noqa: E501
        :rtype: AmazonCloudFeatures
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute(self):
        """Gets the compute of this AmazonCloudFeatures.


        :return: The compute of this AmazonCloudFeatures.
        :rtype: bool
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this AmazonCloudFeatures.


        :param compute: The compute of this AmazonCloudFeatures.
        :type compute: bool
        """

        self._compute = compute

    @property
    def dns(self):
        """Gets the dns of this AmazonCloudFeatures.


        :return: The dns of this AmazonCloudFeatures.
        :rtype: bool
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this AmazonCloudFeatures.


        :param dns: The dns of this AmazonCloudFeatures.
        :type dns: bool
        """

        self._dns = dns

    @property
    def container(self):
        """Gets the container of this AmazonCloudFeatures.


        :return: The container of this AmazonCloudFeatures.
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this AmazonCloudFeatures.


        :param container: The container of this AmazonCloudFeatures.
        :type container: bool
        """

        self._container = container

    @property
    def objectstorage(self):
        """Gets the objectstorage of this AmazonCloudFeatures.


        :return: The objectstorage of this AmazonCloudFeatures.
        :rtype: bool
        """
        return self._objectstorage

    @objectstorage.setter
    def objectstorage(self, objectstorage):
        """Sets the objectstorage of this AmazonCloudFeatures.


        :param objectstorage: The objectstorage of this AmazonCloudFeatures.
        :type objectstorage: bool
        """

        self._objectstorage = objectstorage
