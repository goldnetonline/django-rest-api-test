'''
File: default_backend.py
Project: token-credit-backend
File Created: Wednesday, 29th January 2020 10:05:45 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 10:56:17 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from support.models.mixims import TouchDatesMixim
from support.storages import default_backend
from stdimage import StdImageField


# from .model import Application

class UserGender(Enum):
    MALE = "male"
    FEMALE = "female"


class UserMaritalStatus(Enum):
    SINGLE = 'single'
    MARRIED = 'married'
    DIVERCOED = 'diverced'
    WIDOW = 'widow'


genders: list = [(g.value, g.value.title()) for g in UserGender]

marital_statuses: list = [(m.value, m.value.title())
                          for m in UserMaritalStatus]


class UserManager(BaseUserManager):
    """
    Custom Model Manager for the User Model
    """

    def create_user(self, email: str, password: str = None, **extra_fields):
        """Create new user

        Args:
            email (str): The user email
            password (str, optional): The password. Defaults to None.

        Raises:
            ValueError: if the email is not provided
        """

        if not email:
            raise ValueError("Email is required")

        if not password:
            password = self.make_random_password()

        email = self.normalize_email(email)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('username', email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        # This is a must
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractUser, TouchDatesMixim):
    """The User Model"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name'
    ]

    HIDDEN = [
        'password', 'groups', 'user_permissions'
    ]

    email = models.EmailField("email address", max_length=191, unique=True)
    phone = models.CharField(max_length=191, null=True, blank=True)

    gender = models.CharField(
        choices=genders, max_length=20, blank=True, null=True)

    marital_status = models.CharField(
        choices=marital_statuses, max_length=20, blank=True, null=True)

    birthday = models.DateField(blank=True, null=True)

    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=191, null=True, blank=True)
    state = models.CharField(max_length=191, null=True, blank=True)
    country = models.CharField(max_length=191, null=True, blank=True)

    avatar = StdImageField(
        storage=default_backend, upload_to='avatars',
        verbose_name="Profile Picture",
        variations={
            # 'main': (400, 500),
            'large': (1024, 1024, True),
            'medium': (500, 500, True),
            'thumb': (200, 200, True),
        }, delete_orphans=True,
        null=True, blank=True)

    must_change_password = models.BooleanField(
        blank=True, null=True, default=False)

    is_blocked = models.BooleanField(blank=True, null=True, default=False)

    apply_ban_lifted = models.BooleanField(
        blank=True, null=True, default=False)

    lead_source_id = models.PositiveIntegerField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        db_table = 'users'

    @property
    def name(self) -> str:
        """get the full name of user"""
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self) -> str:
        return self.name()

    def get_short_name(self) -> str:
        return self.first_name

    def __str__(self):
        return f"{self.name} ({self.email})"


UserModel = get_user_model()
