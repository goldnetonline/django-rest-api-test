'''
File: s3_private.py
Project: edutours.com.ng
File Created: Thursday, 20th February 2020 2:18:32 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Friday, 8th May 2020 8:07:16 pm
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
