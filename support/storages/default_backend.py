'''
File: user.py
Project: token-credit-backend
File Created: Thursday, 20th February 2020 3:09:51 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:02 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from ..helper import config, getClassFromDotString

defaultStorage = config('DEFAULT_FILE_STORAGE')


class DefautStorageBackend:
    default_backend = None
    instance = None

    def __init__(self):
        if not defaultStorage:
            raise Exception('Default storage backend not configured')

        self.default_backend = getClassFromDotString(defaultStorage)()

    @property
    def backend(self):
        return self.default_backend

    @staticmethod
    def getInstance():
        if not DefautStorageBackend.instance:
            DefautStorageBackend.instance = (DefautStorageBackend()).backend
        return DefautStorageBackend.instance


defaultBackend = DefautStorageBackend.getInstance()

__all__ = [
    'defaultBackend'
]
