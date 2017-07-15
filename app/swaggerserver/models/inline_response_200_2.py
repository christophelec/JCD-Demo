# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2002(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code: int=None, type: str=None, message: str=None):
        """
        InlineResponse2002 - a model defined in Swagger

        :param code: The code of this InlineResponse2002.
        :type code: int
        :param type: The type of this InlineResponse2002.
        :type type: str
        :param message: The message of this InlineResponse2002.
        :type message: str
        """
        self.swagger_types = {
            'code': int,
            'type': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type',
            'message': 'message'
        }

        self._code = code
        self._type = type
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.
        :rtype: InlineResponse2002
        """
        return deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """
        Gets the code of this InlineResponse2002.

        :return: The code of this InlineResponse2002.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """
        Sets the code of this InlineResponse2002.

        :param code: The code of this InlineResponse2002.
        :type code: int
        """

        self._code = code

    @property
    def type(self) -> str:
        """
        Gets the type of this InlineResponse2002.

        :return: The type of this InlineResponse2002.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this InlineResponse2002.

        :param type: The type of this InlineResponse2002.
        :type type: str
        """

        self._type = type

    @property
    def message(self) -> str:
        """
        Gets the message of this InlineResponse2002.

        :return: The message of this InlineResponse2002.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this InlineResponse2002.

        :param message: The message of this InlineResponse2002.
        :type message: str
        """

        self._message = message
