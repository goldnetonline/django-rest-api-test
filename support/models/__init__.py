'''
File: user.py
Project: token-credit-backend
File Created: Sunday, 26th January 2020 12:34:04 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from .mixims import TouchDatesMixim, SlugifyMixim
from .setting import SiteSetting
from .email import EmailTemplate

__all__ = [
    TouchDatesMixim,
    SlugifyMixim,
    SiteSetting,
    EmailTemplate
]
