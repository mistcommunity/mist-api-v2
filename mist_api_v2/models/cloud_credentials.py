# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.alibaba_credentials import AlibabaCredentials
from mist_api_v2.models.amazon_credentials import AmazonCredentials
from mist_api_v2.models.azure_credentials import AzureCredentials
from mist_api_v2.models.cloud_sigma_credentials import CloudSigmaCredentials
from mist_api_v2.models.digitalocean_credentials import DigitaloceanCredentials
from mist_api_v2.models.docker_credentials import DockerCredentials
from mist_api_v2.models.equinix_credentials import EquinixCredentials
from mist_api_v2.models.google_credentials import GoogleCredentials
from mist_api_v2.models.ibm_credentials import IbmCredentials
from mist_api_v2.models.kubevirt_credentials import KubevirtCredentials
from mist_api_v2.models.linode_credentials import LinodeCredentials
from mist_api_v2.models.lxd_credentials import LxdCredentials
from mist_api_v2.models.maxihost_credentials import MaxihostCredentials
from mist_api_v2.models.onapp_credentials import OnappCredentials
from mist_api_v2.models.openstack_credentials import OpenstackCredentials
from mist_api_v2.models.rackspace_credentials import RackspaceCredentials
from mist_api_v2.models.vsphere_credentials import VsphereCredentials
from mist_api_v2.models.vultr_credentials import VultrCredentials
from mist_api_v2 import util

from mist_api_v2.models.alibaba_credentials import AlibabaCredentials  # noqa: E501
from mist_api_v2.models.amazon_credentials import AmazonCredentials  # noqa: E501
from mist_api_v2.models.azure_credentials import AzureCredentials  # noqa: E501
from mist_api_v2.models.cloud_sigma_credentials import CloudSigmaCredentials  # noqa: E501
from mist_api_v2.models.digitalocean_credentials import DigitaloceanCredentials  # noqa: E501
from mist_api_v2.models.docker_credentials import DockerCredentials  # noqa: E501
from mist_api_v2.models.equinix_credentials import EquinixCredentials  # noqa: E501
from mist_api_v2.models.google_credentials import GoogleCredentials  # noqa: E501
from mist_api_v2.models.ibm_credentials import IbmCredentials  # noqa: E501
from mist_api_v2.models.kubevirt_credentials import KubevirtCredentials  # noqa: E501
from mist_api_v2.models.linode_credentials import LinodeCredentials  # noqa: E501
from mist_api_v2.models.lxd_credentials import LxdCredentials  # noqa: E501
from mist_api_v2.models.maxihost_credentials import MaxihostCredentials  # noqa: E501
from mist_api_v2.models.onapp_credentials import OnappCredentials  # noqa: E501
from mist_api_v2.models.openstack_credentials import OpenstackCredentials  # noqa: E501
from mist_api_v2.models.rackspace_credentials import RackspaceCredentials  # noqa: E501
from mist_api_v2.models.vsphere_credentials import VsphereCredentials  # noqa: E501
from mist_api_v2.models.vultr_credentials import VultrCredentials  # noqa: E501

class CloudCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, apikey=None, apisecret=None, region=None, tenant_id=None, subscription_id=None, key=None, secret=None, project_id=None, private_key=None, username=None, password=None, provider=None, token=None, auth_url=None, user=None, tenant=None, domain=None, compute_endpoint=None, host=None, verify=None, ca_cert_file=None, port=None, tls_key=None, tls_cert=None, tls_ca_cert=None, show_all=None):  # noqa: E501
        """CloudCredentials - a model defined in OpenAPI

        :param apikey: The apikey of this CloudCredentials.  # noqa: E501
        :type apikey: str
        :param apisecret: The apisecret of this CloudCredentials.  # noqa: E501
        :type apisecret: str
        :param region: The region of this CloudCredentials.  # noqa: E501
        :type region: str
        :param tenant_id: The tenant_id of this CloudCredentials.  # noqa: E501
        :type tenant_id: str
        :param subscription_id: The subscription_id of this CloudCredentials.  # noqa: E501
        :type subscription_id: str
        :param key: The key of this CloudCredentials.  # noqa: E501
        :type key: str
        :param secret: The secret of this CloudCredentials.  # noqa: E501
        :type secret: str
        :param project_id: The project_id of this CloudCredentials.  # noqa: E501
        :type project_id: str
        :param private_key: The private_key of this CloudCredentials.  # noqa: E501
        :type private_key: str
        :param username: The username of this CloudCredentials.  # noqa: E501
        :type username: str
        :param password: The password of this CloudCredentials.  # noqa: E501
        :type password: str
        :param provider: The provider of this CloudCredentials.  # noqa: E501
        :type provider: str
        :param token: The token of this CloudCredentials.  # noqa: E501
        :type token: str
        :param auth_url: The auth_url of this CloudCredentials.  # noqa: E501
        :type auth_url: str
        :param user: The user of this CloudCredentials.  # noqa: E501
        :type user: str
        :param tenant: The tenant of this CloudCredentials.  # noqa: E501
        :type tenant: str
        :param domain: The domain of this CloudCredentials.  # noqa: E501
        :type domain: str
        :param compute_endpoint: The compute_endpoint of this CloudCredentials.  # noqa: E501
        :type compute_endpoint: str
        :param host: The host of this CloudCredentials.  # noqa: E501
        :type host: str
        :param verify: The verify of this CloudCredentials.  # noqa: E501
        :type verify: bool
        :param ca_cert_file: The ca_cert_file of this CloudCredentials.  # noqa: E501
        :type ca_cert_file: str
        :param port: The port of this CloudCredentials.  # noqa: E501
        :type port: str
        :param tls_key: The tls_key of this CloudCredentials.  # noqa: E501
        :type tls_key: str
        :param tls_cert: The tls_cert of this CloudCredentials.  # noqa: E501
        :type tls_cert: str
        :param tls_ca_cert: The tls_ca_cert of this CloudCredentials.  # noqa: E501
        :type tls_ca_cert: str
        :param show_all: The show_all of this CloudCredentials.  # noqa: E501
        :type show_all: bool
        """
        self.openapi_types = {
            'apikey': str,
            'apisecret': str,
            'region': str,
            'tenant_id': str,
            'subscription_id': str,
            'key': str,
            'secret': str,
            'project_id': str,
            'private_key': str,
            'username': str,
            'password': str,
            'provider': str,
            'token': str,
            'auth_url': str,
            'user': str,
            'tenant': str,
            'domain': str,
            'compute_endpoint': str,
            'host': str,
            'verify': bool,
            'ca_cert_file': str,
            'port': str,
            'tls_key': str,
            'tls_cert': str,
            'tls_ca_cert': str,
            'show_all': bool
        }

        self.attribute_map = {
            'apikey': 'apikey',
            'apisecret': 'apisecret',
            'region': 'region',
            'tenant_id': 'tenantId',
            'subscription_id': 'subscriptionId',
            'key': 'key',
            'secret': 'secret',
            'project_id': 'projectId',
            'private_key': 'privateKey',
            'username': 'username',
            'password': 'password',
            'provider': 'provider',
            'token': 'token',
            'auth_url': 'authUrl',
            'user': 'user',
            'tenant': 'tenant',
            'domain': 'domain',
            'compute_endpoint': 'computeEndpoint',
            'host': 'host',
            'verify': 'verify',
            'ca_cert_file': 'ca_cert_file',
            'port': 'port',
            'tls_key': 'tlsKey',
            'tls_cert': 'tlsCert',
            'tls_ca_cert': 'tlsCaCert',
            'show_all': 'showAll'
        }

        self._apikey = apikey
        self._apisecret = apisecret
        self._region = region
        self._tenant_id = tenant_id
        self._subscription_id = subscription_id
        self._key = key
        self._secret = secret
        self._project_id = project_id
        self._private_key = private_key
        self._username = username
        self._password = password
        self._provider = provider
        self._token = token
        self._auth_url = auth_url
        self._user = user
        self._tenant = tenant
        self._domain = domain
        self._compute_endpoint = compute_endpoint
        self._host = host
        self._verify = verify
        self._ca_cert_file = ca_cert_file
        self._port = port
        self._tls_key = tls_key
        self._tls_cert = tls_cert
        self._tls_ca_cert = tls_ca_cert
        self._show_all = show_all

    @classmethod
    def from_dict(cls, dikt) -> 'CloudCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CloudCredentials of this CloudCredentials.  # noqa: E501
        :rtype: CloudCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def apikey(self):
        """Gets the apikey of this CloudCredentials.


        :return: The apikey of this CloudCredentials.
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """Sets the apikey of this CloudCredentials.


        :param apikey: The apikey of this CloudCredentials.
        :type apikey: str
        """
        if apikey is None:
            raise ValueError("Invalid value for `apikey`, must not be `None`")  # noqa: E501

        self._apikey = apikey

    @property
    def apisecret(self):
        """Gets the apisecret of this CloudCredentials.

        Your Alibaba Cloud API secret  # noqa: E501

        :return: The apisecret of this CloudCredentials.
        :rtype: str
        """
        return self._apisecret

    @apisecret.setter
    def apisecret(self, apisecret):
        """Sets the apisecret of this CloudCredentials.

        Your Alibaba Cloud API secret  # noqa: E501

        :param apisecret: The apisecret of this CloudCredentials.
        :type apisecret: str
        """
        if apisecret is None:
            raise ValueError("Invalid value for `apisecret`, must not be `None`")  # noqa: E501

        self._apisecret = apisecret

    @property
    def region(self):
        """Gets the region of this CloudCredentials.


        :return: The region of this CloudCredentials.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudCredentials.


        :param region: The region of this CloudCredentials.
        :type region: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CloudCredentials.

        Your Azure tenant ID  # noqa: E501

        :return: The tenant_id of this CloudCredentials.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CloudCredentials.

        Your Azure tenant ID  # noqa: E501

        :param tenant_id: The tenant_id of this CloudCredentials.
        :type tenant_id: str
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CloudCredentials.

        Your Azure subscription ID  # noqa: E501

        :return: The subscription_id of this CloudCredentials.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CloudCredentials.

        Your Azure subscription ID  # noqa: E501

        :param subscription_id: The subscription_id of this CloudCredentials.
        :type subscription_id: str
        """
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def key(self):
        """Gets the key of this CloudCredentials.

        Your Azure key  # noqa: E501

        :return: The key of this CloudCredentials.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CloudCredentials.

        Your Azure key  # noqa: E501

        :param key: The key of this CloudCredentials.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def secret(self):
        """Gets the secret of this CloudCredentials.

        Your Azure secret  # noqa: E501

        :return: The secret of this CloudCredentials.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this CloudCredentials.

        Your Azure secret  # noqa: E501

        :param secret: The secret of this CloudCredentials.
        :type secret: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def project_id(self):
        """Gets the project_id of this CloudCredentials.

        The Id of your GCP project  # noqa: E501

        :return: The project_id of this CloudCredentials.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CloudCredentials.

        The Id of your GCP project  # noqa: E501

        :param project_id: The project_id of this CloudCredentials.
        :type project_id: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def private_key(self):
        """Gets the private_key of this CloudCredentials.

        Your GCP private key  # noqa: E501

        :return: The private_key of this CloudCredentials.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CloudCredentials.

        Your GCP private key  # noqa: E501

        :param private_key: The private_key of this CloudCredentials.
        :type private_key: str
        """
        if private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")  # noqa: E501

        self._private_key = private_key

    @property
    def username(self):
        """Gets the username of this CloudCredentials.

        Your Kubernetes API username  # noqa: E501

        :return: The username of this CloudCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CloudCredentials.

        Your Kubernetes API username  # noqa: E501

        :param username: The username of this CloudCredentials.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this CloudCredentials.

        Your Kubernetes API password  # noqa: E501

        :return: The password of this CloudCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CloudCredentials.

        Your Kubernetes API password  # noqa: E501

        :param password: The password of this CloudCredentials.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def provider(self):
        """Gets the provider of this CloudCredentials.


        :return: The provider of this CloudCredentials.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CloudCredentials.


        :param provider: The provider of this CloudCredentials.
        :type provider: str
        """
        allowed_values = ["rackspace"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def token(self):
        """Gets the token of this CloudCredentials.

        Your Kubernetes API bearer token  # noqa: E501

        :return: The token of this CloudCredentials.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CloudCredentials.

        Your Kubernetes API bearer token  # noqa: E501

        :param token: The token of this CloudCredentials.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def auth_url(self):
        """Gets the auth_url of this CloudCredentials.


        :return: The auth_url of this CloudCredentials.
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this CloudCredentials.


        :param auth_url: The auth_url of this CloudCredentials.
        :type auth_url: str
        """
        if auth_url is None:
            raise ValueError("Invalid value for `auth_url`, must not be `None`")  # noqa: E501

        self._auth_url = auth_url

    @property
    def user(self):
        """Gets the user of this CloudCredentials.


        :return: The user of this CloudCredentials.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CloudCredentials.


        :param user: The user of this CloudCredentials.
        :type user: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def tenant(self):
        """Gets the tenant of this CloudCredentials.


        :return: The tenant of this CloudCredentials.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this CloudCredentials.


        :param tenant: The tenant of this CloudCredentials.
        :type tenant: str
        """

        self._tenant = tenant

    @property
    def domain(self):
        """Gets the domain of this CloudCredentials.


        :return: The domain of this CloudCredentials.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CloudCredentials.


        :param domain: The domain of this CloudCredentials.
        :type domain: str
        """

        self._domain = domain

    @property
    def compute_endpoint(self):
        """Gets the compute_endpoint of this CloudCredentials.


        :return: The compute_endpoint of this CloudCredentials.
        :rtype: str
        """
        return self._compute_endpoint

    @compute_endpoint.setter
    def compute_endpoint(self, compute_endpoint):
        """Sets the compute_endpoint of this CloudCredentials.


        :param compute_endpoint: The compute_endpoint of this CloudCredentials.
        :type compute_endpoint: str
        """

        self._compute_endpoint = compute_endpoint

    @property
    def host(self):
        """Gets the host of this CloudCredentials.

        Your Kubernetes API host  # noqa: E501

        :return: The host of this CloudCredentials.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CloudCredentials.

        Your Kubernetes API host  # noqa: E501

        :param host: The host of this CloudCredentials.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def verify(self):
        """Gets the verify of this CloudCredentials.


        :return: The verify of this CloudCredentials.
        :rtype: bool
        """
        return self._verify

    @verify.setter
    def verify(self, verify):
        """Sets the verify of this CloudCredentials.


        :param verify: The verify of this CloudCredentials.
        :type verify: bool
        """

        self._verify = verify

    @property
    def ca_cert_file(self):
        """Gets the ca_cert_file of this CloudCredentials.

        CA certificate  # noqa: E501

        :return: The ca_cert_file of this CloudCredentials.
        :rtype: str
        """
        return self._ca_cert_file

    @ca_cert_file.setter
    def ca_cert_file(self, ca_cert_file):
        """Sets the ca_cert_file of this CloudCredentials.

        CA certificate  # noqa: E501

        :param ca_cert_file: The ca_cert_file of this CloudCredentials.
        :type ca_cert_file: str
        """

        self._ca_cert_file = ca_cert_file

    @property
    def port(self):
        """Gets the port of this CloudCredentials.

        Your Kubernetes API port  # noqa: E501

        :return: The port of this CloudCredentials.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CloudCredentials.

        Your Kubernetes API port  # noqa: E501

        :param port: The port of this CloudCredentials.
        :type port: str
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def tls_key(self):
        """Gets the tls_key of this CloudCredentials.

        Your TLS auth key  # noqa: E501

        :return: The tls_key of this CloudCredentials.
        :rtype: str
        """
        return self._tls_key

    @tls_key.setter
    def tls_key(self, tls_key):
        """Sets the tls_key of this CloudCredentials.

        Your TLS auth key  # noqa: E501

        :param tls_key: The tls_key of this CloudCredentials.
        :type tls_key: str
        """

        self._tls_key = tls_key

    @property
    def tls_cert(self):
        """Gets the tls_cert of this CloudCredentials.

        Your TLS auth certificate  # noqa: E501

        :return: The tls_cert of this CloudCredentials.
        :rtype: str
        """
        return self._tls_cert

    @tls_cert.setter
    def tls_cert(self, tls_cert):
        """Sets the tls_cert of this CloudCredentials.

        Your TLS auth certificate  # noqa: E501

        :param tls_cert: The tls_cert of this CloudCredentials.
        :type tls_cert: str
        """

        self._tls_cert = tls_cert

    @property
    def tls_ca_cert(self):
        """Gets the tls_ca_cert of this CloudCredentials.

        Your TLS CA certifcate  # noqa: E501

        :return: The tls_ca_cert of this CloudCredentials.
        :rtype: str
        """
        return self._tls_ca_cert

    @tls_ca_cert.setter
    def tls_ca_cert(self, tls_ca_cert):
        """Sets the tls_ca_cert of this CloudCredentials.

        Your TLS CA certifcate  # noqa: E501

        :param tls_ca_cert: The tls_ca_cert of this CloudCredentials.
        :type tls_ca_cert: str
        """

        self._tls_ca_cert = tls_ca_cert

    @property
    def show_all(self):
        """Gets the show_all of this CloudCredentials.

        Show all containers, including stopped  # noqa: E501

        :return: The show_all of this CloudCredentials.
        :rtype: bool
        """
        return self._show_all

    @show_all.setter
    def show_all(self, show_all):
        """Sets the show_all of this CloudCredentials.

        Show all containers, including stopped  # noqa: E501

        :param show_all: The show_all of this CloudCredentials.
        :type show_all: bool
        """

        self._show_all = show_all
