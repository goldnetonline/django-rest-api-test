'''
File: user.py
Project: token-credit-backend
File Created: Monday, 2nd November 2020 11:41:53 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 11:44:59 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from core.models.user import UserModel

from rest_framework import viewsets, permissions
from ..serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User rest view
    """
    queryset = UserModel.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
