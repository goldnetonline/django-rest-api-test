'''
File: user.py
Project: token-credit-backend
File Created: Tuesday, 7th July 2020 5:03:12 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='naira')
@stringfilter
def naira(text):
    """
    Prepend naira sign to a currency text
    Ensure to add the naira to the last of the stack

    Args:
        text (str): The currency text

    Returns:
        str: The text with prepanded naira
    """
    return f"₦{text}"
