'''
File: user.py
Project: token-credit-backend
File Created: Tuesday, 25th February 2020 7:17:35 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from django.db.models import Model
from django.shortcuts import get_object_or_404


def findOrFail(model: Model, **kwargs):
    return get_object_or_404(model, **kwargs)
