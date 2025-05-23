# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mist_api_v2.models.base_model_ import Model
from mist_api_v2.models.action import Action
from mist_api_v2.models.condition import Condition
from mist_api_v2.models.selector import Selector
from mist_api_v2.models.trigger_after import TriggerAfter
from mist_api_v2.models.when import When
from mist_api_v2 import util

from mist_api_v2.models.action import Action  # noqa: E501
from mist_api_v2.models.condition import Condition  # noqa: E501
from mist_api_v2.models.selector import Selector  # noqa: E501
from mist_api_v2.models.trigger_after import TriggerAfter  # noqa: E501
from mist_api_v2.models.when import When  # noqa: E501

class Rule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, selectors=None, conditions=None, actions=None, when=None, trigger_after=None):  # noqa: E501
        """Rule - a model defined in OpenAPI

        :param id: The id of this Rule.  # noqa: E501
        :type id: str
        :param name: The name of this Rule.  # noqa: E501
        :type name: str
        :param description: The description of this Rule.  # noqa: E501
        :type description: str
        :param selectors: The selectors of this Rule.  # noqa: E501
        :type selectors: List[Selector]
        :param conditions: The conditions of this Rule.  # noqa: E501
        :type conditions: List[Condition]
        :param actions: The actions of this Rule.  # noqa: E501
        :type actions: List[Action]
        :param when: The when of this Rule.  # noqa: E501
        :type when: When
        :param trigger_after: The trigger_after of this Rule.  # noqa: E501
        :type trigger_after: TriggerAfter
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'selectors': List[Selector],
            'conditions': List[Condition],
            'actions': List[Action],
            'when': When,
            'trigger_after': TriggerAfter
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'selectors': 'selectors',
            'conditions': 'conditions',
            'actions': 'actions',
            'when': 'when',
            'trigger_after': 'trigger_after'
        }

        self._id = id
        self._name = name
        self._description = description
        self._selectors = selectors
        self._conditions = conditions
        self._actions = actions
        self._when = when
        self._trigger_after = trigger_after

    @classmethod
    def from_dict(cls, dikt) -> 'Rule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rule of this Rule.  # noqa: E501
        :rtype: Rule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Rule.


        :return: The id of this Rule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rule.


        :param id: The id of this Rule.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Rule.


        :return: The name of this Rule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.


        :param name: The name of this Rule.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.


        :return: The description of this Rule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.


        :param description: The description of this Rule.
        :type description: str
        """

        self._description = description

    @property
    def selectors(self):
        """Gets the selectors of this Rule.


        :return: The selectors of this Rule.
        :rtype: List[Selector]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this Rule.


        :param selectors: The selectors of this Rule.
        :type selectors: List[Selector]
        """

        self._selectors = selectors

    @property
    def conditions(self):
        """Gets the conditions of this Rule.


        :return: The conditions of this Rule.
        :rtype: List[Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Rule.


        :param conditions: The conditions of this Rule.
        :type conditions: List[Condition]
        """

        self._conditions = conditions

    @property
    def actions(self):
        """Gets the actions of this Rule.


        :return: The actions of this Rule.
        :rtype: List[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Rule.


        :param actions: The actions of this Rule.
        :type actions: List[Action]
        """

        self._actions = actions

    @property
    def when(self):
        """Gets the when of this Rule.


        :return: The when of this Rule.
        :rtype: When
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this Rule.


        :param when: The when of this Rule.
        :type when: When
        """

        self._when = when

    @property
    def trigger_after(self):
        """Gets the trigger_after of this Rule.


        :return: The trigger_after of this Rule.
        :rtype: TriggerAfter
        """
        return self._trigger_after

    @trigger_after.setter
    def trigger_after(self, trigger_after):
        """Sets the trigger_after of this Rule.


        :param trigger_after: The trigger_after of this Rule.
        :type trigger_after: TriggerAfter
        """

        self._trigger_after = trigger_after
