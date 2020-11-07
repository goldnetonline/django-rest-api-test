'''
File: user.py
Project: token-credit-backend
File Created: Monday, 22nd June 2020 5:45:33 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Wednesday, 28th October 2020 1:01:01 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from django import template
from django.template.defaultfilters import stringfilter
from os import path
from json import loads
register = template.Library()


@register.filter(name='mix_asset')
@stringfilter
def mix_asset(url):
    from ..helper import config
    static_backend = config('STATICFILES_STORAGE')
    static_url = config('STATIC_URL')
    base_dir = config('BASE_DIR')
    link = url if not url.startswith('/') else url[1:]
    manifest_path = path.join(
        base_dir,
        static_url if not static_url.startswith('/') else static_url[1:],
        'mix-manifest.json'
    )

    # If using local backend
    if static_backend == 'django.contrib.staticfiles.storage.StaticFilesStorage':
        try:
            with open(manifest_path, 'r') as man_file:
                manifest = man_file.read()
                serializer = loads(manifest)
                if("/" + link in serializer):
                    link = serializer.get("/" + url)
                    if(link.startswith('/')):
                        link = link[1:]
        except FileNotFoundError | AttributeError:
            pass

    return static_url + link
