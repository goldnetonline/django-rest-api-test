'''
File: model.py
Project: edutours.com.ng
File Created: Tuesday, 25th February 2020 7:17:35 pm
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Tuesday, 25th February 2020 7:21:52 pm
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
'''

from django.db.models import Model
from django.shortcuts import get_object_or_404


def findOrFail(model: Model, **kwargs):
    return get_object_or_404(model, **kwargs)
