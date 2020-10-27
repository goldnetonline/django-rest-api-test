'''
File: __init__.py
Project: edutours.com.ng
File Created: Sunday, 26th January 2020 12:34:04 am
Author: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Last Modified: Thursday, 27th February 2020 9:26:04 am
Modified By: Temitayo Bodunrin (temitayo@brandnaware.com)
-----
Copyright 2020, Brandnaware Nigeria
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
