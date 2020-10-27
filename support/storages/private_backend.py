from . import S3Private, MinioPrivate
from ..helper import config

env = config('APP_ENV')


class PrivateBackend:
    backend = None
    instance = None

    def __init__(self):
        if(env == 'local'):
            self.backend = MinioPrivate
        else:
            self.backend = S3Private

    @staticmethod
    def getInstance():
        if not PrivateBackend.instance:
            PrivateBackend.instance = (PrivateBackend()).backend()
        return PrivateBackend.instance


privateBackend = PrivateBackend.getInstance()

__all__ = [
    'privateBackend',
    'PrivateBackend'
]
