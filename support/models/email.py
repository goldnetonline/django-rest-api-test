'''
File: email.py
Project: token-credit-backend
File Created: Thursday, 27th February 2020 7:03:50 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Tuesday, 27th October 2020 12:48:36 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from django.db import models
from . import TouchDatesMixim, SlugifyMixim, SiteSetting
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist


class EmailTemplate(TouchDatesMixim, SlugifyMixim):
    name = models.CharField(max_length=191)
    subject = models.CharField(max_length=191)
    message = models.TextField(
        help_text='Please do not put a beginning salutation like dear ..., or closing greetings like regards as this will be taken care of. \n<br />\
            However, you can use the following anywhere to reference values: <br />\n\
            {{ applicant_name }} : Add appplicant name  <br />\n  \
            {{ institution }} : The institution applied for if any   \
        You can use HTML'
    )

    def __str__(self):
        return self.name

    @property
    def html_message(self):
        return self.message.replace('\n', '<br />')

    @classmethod
    def fromSetting(cls, email: str = 'pending_email'):
        """Get an email template from setting

        Args:
            email (str, optional): The email template identifier string. Defaults to 'pending_email'.

        Returns:
            EmailTemplate: Email template object
        """
        theEmail = None
        emailSetting = SiteSetting.get_by_name(email)

        if not emailSetting:
            return None
        try:
            theEmail = cls.objects.get(pk=int(emailSetting))
        except DoesNotExist:
            return None

        return theEmail
