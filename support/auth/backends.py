'''
File: backends.py
Project: edutours.com.ng
File Created: Wednesday, 19th February 2020 5:09:55 pm
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Wednesday, 19th February 2020 5:59:47 pm
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
'''
from django.contrib.auth.backends import BaseBackend
from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_user_model():
    """
    Return the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )


UserModel = get_user_model()


class UserBackend(BaseBackend):
    """
    A custom authentication backend that separate from django's default
    it used the SETTINGS.USER_MODEL as base model
    """

    def authenticate(self, request, email=None, password=None, **kwargs):

        if email is None or password is None:
            return None
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self._user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None

    def _user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """

        # for now return true except you have other plans
        return True
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None
