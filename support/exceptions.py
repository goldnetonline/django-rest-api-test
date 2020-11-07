'''
File: user.py
Project: token-credit-backend
File Created: Friday, 26th June 2020 2:03:52 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''


class ExceptionBase(Exception):
    default_message = 'Error'

    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(msg if msg else self.default_message, *args, **kwargs)


class NoOrInvalidPaystackKey(ExceptionBase):
    default_message = "Invalid or no paystack secret key supplied"


class Forbidden(ExceptionBase):
    default_message = "403 Forbidden Kingdom"
