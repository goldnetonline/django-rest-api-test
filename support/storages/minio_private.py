'''
File: minio_private.py
Project: edutours.com.ng
File Created: Thursday, 20th February 2020 2:29:49 pm
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Thursday, 20th February 2020 2:33:17 pm
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
'''

from minio_storage.storage import MinioMediaStorage
from ..helper import config

privateBucket = config('PRIVATE_BUCKET')


class MinioPrivate(MinioMediaStorage):
    pass
