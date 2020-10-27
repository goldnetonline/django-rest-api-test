'''
File: __init__.py
Project: edutours.com.ng
File Created: Sunday, 26th January 2020 12:34:04 am
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Thursday, 20th February 2020 4:16:07 pm
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
'''
from .s3_private import S3Private
from .minio_private import MinioPrivate
from .default_backend import defaultBackend
from .private_backend import privateBackend, PrivateBackend

__all__ = ['S3Private', 'MinioPrivate',
           'defaultBackend', 'privateBackend', 'PrivateBackend']
