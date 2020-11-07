'''
File: user.py
Project: token-credit-backend
File Created: Thursday, 20th February 2020 2:18:32 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:02 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from storages.backends.s3boto3 import S3Boto3Storage
from ..helper import config

privateBucket = config('AWS_PRIVATE_BUCKET')
privateLocation = config('AWS_PRIVATE_BUCKET_URL')


class S3Private(S3Boto3Storage):
    bucket_name = privateBucket
    bucket_acl = 'private'
    file_overwrite = False
    querystring_auth = True
    endpoint_url = privateLocation
    signature_version = 's3v4'
