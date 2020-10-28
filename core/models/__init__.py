'''
File: __init__.py
Project: token-credit-backend
File Created: Wednesday, 28th October 2020 6:32:26 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 2:23:16 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from .user import User, UserGender, UserMaritalStatus

__all__ = [
    User, UserGender, UserMaritalStatus
]
