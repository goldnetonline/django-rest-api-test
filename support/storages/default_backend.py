'''
File: default_backend.py
Project: edutours.com.ng
File Created: Thursday, 20th February 2020 3:09:51 pm
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Thursday, 20th February 2020 4:13:41 pm
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
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
