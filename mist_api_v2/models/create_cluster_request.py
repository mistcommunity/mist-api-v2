# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.cluster_providers import ClusterProviders
from mist_api_v2.models.create_cluster_request_all_of import CreateClusterRequestAllOf
from mist_api_v2.models.create_cluster_request_all_of_nodepools import CreateClusterRequestAllOfNodepools
from mist_api_v2.models.create_cluster_request_all_of_waiters import CreateClusterRequestAllOfWaiters
from mist_api_v2.models.helm_chart import HelmChart
from mist_api_v2.models.kubernetes_manifest import KubernetesManifest
from mist_api_v2 import util

from mist_api_v2.models.cluster_providers import ClusterProviders  # noqa: E501
from mist_api_v2.models.create_cluster_request_all_of import CreateClusterRequestAllOf  # noqa: E501
from mist_api_v2.models.create_cluster_request_all_of_nodepools import CreateClusterRequestAllOfNodepools  # noqa: E501
from mist_api_v2.models.create_cluster_request_all_of_waiters import CreateClusterRequestAllOfWaiters  # noqa: E501
from mist_api_v2.models.helm_chart import HelmChart  # noqa: E501
from mist_api_v2.models.kubernetes_manifest import KubernetesManifest  # noqa: E501

class CreateClusterRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, cloud=None, provider=None, location=None, nodepools=None, templates=None, waiters=None):  # noqa: E501
        """CreateClusterRequest - a model defined in OpenAPI

        :param name: The name of this CreateClusterRequest.  # noqa: E501
        :type name: str
        :param cloud: The cloud of this CreateClusterRequest.  # noqa: E501
        :type cloud: str
        :param provider: The provider of this CreateClusterRequest.  # noqa: E501
        :type provider: ClusterProviders
        :param location: The location of this CreateClusterRequest.  # noqa: E501
        :type location: str
        :param nodepools: The nodepools of this CreateClusterRequest.  # noqa: E501
        :type nodepools: List[CreateClusterRequestAllOfNodepools]
        :param templates: The templates of this CreateClusterRequest.  # noqa: E501
        :type templates: List[object]
        :param waiters: The waiters of this CreateClusterRequest.  # noqa: E501
        :type waiters: List[CreateClusterRequestAllOfWaiters]
        """
        self.openapi_types = {
            'name': str,
            'cloud': str,
            'provider': ClusterProviders,
            'location': str,
            'nodepools': List[CreateClusterRequestAllOfNodepools],
            'templates': List[object],
            'waiters': List[CreateClusterRequestAllOfWaiters]
        }

        self.attribute_map = {
            'name': 'name',
            'cloud': 'cloud',
            'provider': 'provider',
            'location': 'location',
            'nodepools': 'nodepools',
            'templates': 'templates',
            'waiters': 'waiters'
        }

        self._name = name
        self._cloud = cloud
        self._provider = provider
        self._location = location
        self._nodepools = nodepools
        self._templates = templates
        self._waiters = waiters

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClusterRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClusterRequest of this CreateClusterRequest.  # noqa: E501
        :rtype: CreateClusterRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateClusterRequest.

        The name of the cluster to create  # noqa: E501

        :return: The name of this CreateClusterRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateClusterRequest.

        The name of the cluster to create  # noqa: E501

        :param name: The name of this CreateClusterRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cloud(self):
        """Gets the cloud of this CreateClusterRequest.

        The cloud the cluster belongs to  # noqa: E501

        :return: The cloud of this CreateClusterRequest.
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this CreateClusterRequest.

        The cloud the cluster belongs to  # noqa: E501

        :param cloud: The cloud of this CreateClusterRequest.
        :type cloud: str
        """

        self._cloud = cloud

    @property
    def provider(self):
        """Gets the provider of this CreateClusterRequest.


        :return: The provider of this CreateClusterRequest.
        :rtype: ClusterProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateClusterRequest.


        :param provider: The provider of this CreateClusterRequest.
        :type provider: ClusterProviders
        """

        self._provider = provider

    @property
    def location(self):
        """Gets the location of this CreateClusterRequest.

        Google specific parameter(Required).Name or ID of the location to create the cluster in  # noqa: E501

        :return: The location of this CreateClusterRequest.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CreateClusterRequest.

        Google specific parameter(Required).Name or ID of the location to create the cluster in  # noqa: E501

        :param location: The location of this CreateClusterRequest.
        :type location: str
        """

        self._location = location

    @property
    def nodepools(self):
        """Gets the nodepools of this CreateClusterRequest.


        :return: The nodepools of this CreateClusterRequest.
        :rtype: List[CreateClusterRequestAllOfNodepools]
        """
        return self._nodepools

    @nodepools.setter
    def nodepools(self, nodepools):
        """Sets the nodepools of this CreateClusterRequest.


        :param nodepools: The nodepools of this CreateClusterRequest.
        :type nodepools: List[CreateClusterRequestAllOfNodepools]
        """

        self._nodepools = nodepools

    @property
    def templates(self):
        """Gets the templates of this CreateClusterRequest.


        :return: The templates of this CreateClusterRequest.
        :rtype: List[object]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this CreateClusterRequest.


        :param templates: The templates of this CreateClusterRequest.
        :type templates: List[object]
        """

        self._templates = templates

    @property
    def waiters(self):
        """Gets the waiters of this CreateClusterRequest.


        :return: The waiters of this CreateClusterRequest.
        :rtype: List[CreateClusterRequestAllOfWaiters]
        """
        return self._waiters

    @waiters.setter
    def waiters(self, waiters):
        """Sets the waiters of this CreateClusterRequest.


        :param waiters: The waiters of this CreateClusterRequest.
        :type waiters: List[CreateClusterRequestAllOfWaiters]
        """

        self._waiters = waiters
