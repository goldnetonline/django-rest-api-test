'''
File: admin.py
Project: token-credit-backend
File Created: Monday, 2nd November 2020 9:31:46 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 2nd November 2020 9:56:48 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from django.test import TestCase, Client
from django.urls import reverse
from ..models.user import UserModel

TEST_ADMIN_EMAIL = "admin@ADMINMASTER.com"
TEST_ADMIN_PASSWORD = "localHost123+++_"
TEST_ADMIN_FIRST_NAME = "Admin"
TEST_ADMIN_LAST_NAME = "Master"


class AdminTests(TestCase):
    """Admin backoffice test"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = UserModel.objects.create_superuser(
            TEST_ADMIN_EMAIL, TEST_ADMIN_PASSWORD,
            first_name=TEST_ADMIN_FIRST_NAME,
            last_name=TEST_ADMIN_LAST_NAME
        )

        self.client.force_login(self.admin_user)
        self.user = UserModel.objects.create_superuser(
            "blanco@email.com", "psdsd*&^3+++"
        )

    def test_users_listed(self):
        """check if our users are listed on users page on admin"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.admin_user.email)
        self.assertContains(res, self.admin_user.first_name)

    def test_user_edit_page(self):
        """test if the user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        """test if the user add page works"""
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
