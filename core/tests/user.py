'''
File: user.py
Project: token-credit-backend
File Created: Monday, 2nd November 2020 2:32:11 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 9:39:02 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from django.test import TestCase

from ..models.user import UserModel

TEST_USER_EMAIL = "test@EMAIL.com"
TEST_USER_PASSWORD = "localHost123"
TEST_USER_FIRST_NAME = "John"
TEST_USER_LAST_NAME = "Doe"


class UserTests(TestCase):
    """
    User tests
    """

    def setUp(self):
        """User setup"""
        email = TEST_USER_EMAIL
        password = TEST_USER_PASSWORD
        first_name = TEST_USER_FIRST_NAME
        last_name = TEST_USER_LAST_NAME

        UserModel.objects.create_user(
            email, password, first_name=first_name, last_name=last_name)

    def test_create_user(self):
        """Crate a valid user"""

        user = UserModel.objects.get(email=TEST_USER_EMAIL.lower())

        # User exists
        self.assertIsNotNone(user)

        # Email Normalised
        self.assertEqual(user.email, TEST_USER_EMAIL.lower())

        # Password Encrypted
        self.assertTrue(user.check_password(TEST_USER_PASSWORD))

        # first_name and last_name added with kwargs
        self.assertEqual(user.first_name, TEST_USER_FIRST_NAME)
        self.assertEqual(user.last_name, TEST_USER_LAST_NAME)

        # Ensure ordinary user is not a staff or super user
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_require_email(self):
        """If email adress is not provided, raise value error"""
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(None, "slmdsdsldsd")

    def test_create_super_user(self):
        """Check if super user is properly created"""
        su = UserModel.objects.create_superuser("superuser@webmaster.com", "08sm#ksdns3")

        self.assertTrue(su.is_staff)
        self.assertTrue(su.is_superuser)

    def test_admin_user_require_password(self):
        """Super user MUST have a password"""
        with self.assertRaises(ValueError):
            UserModel.objects.create_superuser("superuser@webmaster.com", None)
