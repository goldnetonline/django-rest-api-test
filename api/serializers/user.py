'''
File: user.py
Project: token-credit-backend
File Created: Monday, 2nd November 2020 11:37:13 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 12:56:19 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from rest_framework import serializers
from core.models.user import UserModel


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'gender',
            'marital_status',
            'birthday',
            'address',
            'avatar',
            'is_blocked',
            'apply_ban_lifted'
        ]

    def create(self, validated_data):
        """
        Create a user using the create_user method
        """
        return UserModel.objects.create_user(**validated_data)
