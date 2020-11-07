'''
File: index.py
Project: token-credit-backend
File Created: Thursday, 29th October 2020 2:02:48 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 12:58:59 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from django.urls import (
    path, include
    # re_path,
    # include
)
from rest_framework import routers

from ..controllers import (
    index, user
)


router = routers.DefaultRouter()

# router.register('', index.Home)
router.register(r'users', user.UserViewSet)

app_name = 'api_index'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
