'''
File: user.py
Project: token-credit-backend
File Created: Thursday, 20th February 2020 2:29:49 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from minio_storage.storage import MinioMediaStorage
from ..helper import config

privateBucket = config('PRIVATE_BUCKET')


class MinioPrivate(MinioMediaStorage):
    pass
