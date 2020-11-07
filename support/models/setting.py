'''
File: setting.py
Project: token-credit-backend
File Created: Wednesday, 26th February 2020 6:51:39 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 2:10:45 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
# from typing import Optional
from django.db import models
from .mixims import TouchDatesMixim
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist


class SiteSetting(TouchDatesMixim):
    '''
    Add backend setting functionality to site
    '''

    name = models.CharField(max_length=191)
    value = models.TextField()

    def __str__(self):
        return self.name

    @classmethod
    def get_by_name(cls, name: str, defaultValue=None, bool_value: bool = False):
        """
        Get a site setting b y name

        Args:
            name (str): The name of the setting
            defaultValue (any, optional): The default value. Defaults to None.
            bool_value (bool, optional): Return a boolean value instead of string. \
                Defaults to False.

        Returns:
            str|bool: A string or a boolean value
        """
        value = defaultValue

        try:
            get = cls.objects.get(name=name)
            value = get.value

        except DoesNotExist:
            value = defaultValue

        finally:
            if not bool_value:
                return value

            return value == '1' or value == 'yes'
