'''
File: index.py
Project: token-credit-backend
File Created: Thursday, 29th October 2020 2:06:48 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Thursday, 29th October 2020 2:52:10 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from rest_framework.views import APIView
from support.helper import config
from support.http import successJson
from .. import __version__


class Home(APIView):

    def get(self, request):
        return successJson({
            "version": __version__
        }, f"{config('APP_NAME')} version: {__version__}")
