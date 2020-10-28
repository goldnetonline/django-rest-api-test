'''
File: user.py
Project: token-credit-backend
File Created: Sunday, 26th January 2020 12:34:04 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:02 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from .s3_private import S3Private
from .minio_private import MinioPrivate
from .default_backend import defaultBackend
from .private_backend import privateBackend, PrivateBackend

__all__ = ['S3Private', 'MinioPrivate',
           'defaultBackend', 'privateBackend', 'PrivateBackend']
