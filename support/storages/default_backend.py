'''
File: private_backend.py
Project: token-credit-backend
File Created: Thursday, 20th February 2020 3:09:51 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 12:18:39 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from ..helper import config, get_class_from_dot_string
from ..logging import logger

default_storage = config('DEFAULT_FILE_STORAGE')


class DefautStorageBackend:
    default_backend = None
    instance = None

    def __init__(self):
        if not default_storage:
            raise Exception('Default storage backend not configured')

        self.default_backend = get_class_from_dot_string(default_storage)()

    @property
    def backend(self):
        return self.default_backend

    @staticmethod
    def getInstance():
        if not DefautStorageBackend.instance:
            DefautStorageBackend.instance = (DefautStorageBackend()).backend
        return DefautStorageBackend.instance


try:
    default_backend = DefautStorageBackend.getInstance()
except Exception as e:
    logger.exception(e)
    default_backend = None

__all__ = [
    'default_backend'
]
