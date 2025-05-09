# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2 import util


class GoogleCredentials(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, project_id=None, private_key=None, email=None):  # noqa: E501
        """GoogleCredentials - a model defined in OpenAPI

        :param project_id: The project_id of this GoogleCredentials.  # noqa: E501
        :type project_id: str
        :param private_key: The private_key of this GoogleCredentials.  # noqa: E501
        :type private_key: str
        :param email: The email of this GoogleCredentials.  # noqa: E501
        :type email: str
        """
        self.openapi_types = {
            'project_id': str,
            'private_key': str,
            'email': str
        }

        self.attribute_map = {
            'project_id': 'projectId',
            'private_key': 'privateKey',
            'email': 'email'
        }

        self._project_id = project_id
        self._private_key = private_key
        self._email = email

    @classmethod
    def from_dict(cls, dikt) -> 'GoogleCredentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GoogleCredentials of this GoogleCredentials.  # noqa: E501
        :rtype: GoogleCredentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def project_id(self):
        """Gets the project_id of this GoogleCredentials.

        The Id of your GCP project  # noqa: E501

        :return: The project_id of this GoogleCredentials.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GoogleCredentials.

        The Id of your GCP project  # noqa: E501

        :param project_id: The project_id of this GoogleCredentials.
        :type project_id: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def private_key(self):
        """Gets the private_key of this GoogleCredentials.

        Your GCP private key  # noqa: E501

        :return: The private_key of this GoogleCredentials.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this GoogleCredentials.

        Your GCP private key  # noqa: E501

        :param private_key: The private_key of this GoogleCredentials.
        :type private_key: str
        """
        if private_key is None:
            raise ValueError("Invalid value for `private_key`, must not be `None`")  # noqa: E501

        self._private_key = private_key

    @property
    def email(self):
        """Gets the email of this GoogleCredentials.

        Your GCP client email  # noqa: E501

        :return: The email of this GoogleCredentials.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GoogleCredentials.

        Your GCP client email  # noqa: E501

        :param email: The email of this GoogleCredentials.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
