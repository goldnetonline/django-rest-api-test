'''
File: dataclass.py
Project: token-credit-backend
File Created: Monday, 26th October 2020 11:50:05 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 26th October 2020 11:51:17 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''


class Dataclass:
    """
    Generic data class for creating enumeration classes
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.__class__.__name__
