'''
File: root_context.py
Project: token-credit-backend
File Created: Wednesday, 29th January 2020 3:45:50 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 3:33:24 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from datetime import datetime
from support.helper import config


facebook_app_id = config('FACEBOOK_APP_ID', '')
google_client_id = config('GOOGLE_CLIENT_ID', '')


def root_context(request):
    path = request.path[1:]
    if(path.endswith('/')):
        path = path[:-1]

    ctx = {
        # Also available as csrf_token
        # but this is here for a proof of cocept
        # to show that this contxt file is working
        # 'csrf_tokens': request.COOKIES['csrftoken'],
        'app_name': config('APP_NAME'),
        'developer': 'CamelCase Technologies Limited',
        'env': config('APP_ENV'),
        'now': datetime.now(),
        'page_slug': (path != "") and path or "home",
        'facebook_app_id': facebook_app_id,
        'google_client_id': google_client_id,
        'sample_range': range(5),
    }

    # Glue it to the request so it can be available else where
    # By the way name it ctx so as not to mistakenly override
    # something we didn't create
    request.ctx = ctx
    return ctx
