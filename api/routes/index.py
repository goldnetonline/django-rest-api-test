'''
File: index.py
Project: token-credit-backend
File Created: Thursday, 29th October 2020 2:02:48 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 2:26:20 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from django.urls import (
    path,
    # re_path,
    # include
)

from ..controllers import (
    index
)

app_name = 'api_index'

urlpatterns = [
    path('', index.Home.as_view(), name='home')
]
