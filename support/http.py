'''
File: http.py
Project: token-credit-backend
File Created: Sunday, 26th January 2020 12:34:13 am
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Monday, 26th October 2020 11:24:52 am
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from os import path
import requests
from PIL import Image
from tempfile import gettempdir
from urllib.request import urlretrieve
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.urls import reverse, reverse_lazy
from .helper import randomStringDigits, serialize


def response(content=None):
    '''
    Send a plain response as is

    :param str content: The Response, most likely string
    '''
    if content:
        return HttpResponse(content)
    return HttpResponse()


def redirect(to: str, *args, **kwargs):
    """Redirect to a particular route

    Arguments:
        to str -- The url to redirect to

    Returns:
        HttpResponseRedirect -- HttpResponseRedirect Object
    """
    return HttpResponseRedirect(to, *args, **kwargs)


def route(route: str, params: dict = {}, isLazy: bool = False, * args, **kwargs):
    """Get the django reverse route

    Arguments:
        route {str} -- The route
        params {dict} -- The param if any

    Returns:
        HttpResponse -- HttpResponse Object
    """

    if isLazy:
        return reverse_lazy(route, kwargs=params, *args, **kwargs)

    return reverse(route, kwargs=params, *args, **kwargs)


def json(data: object, raw=False, *args, **kwargs):
    '''
    Send a json response

    :param object data: The Response data
    '''
    if not isinstance(data, dict):
        data = {'message': data}

    if 'additionalFields' in kwargs and isinstance(kwargs['additionalFields'], dict):
        for (key, value) in kwargs.get('additionalFields').items():
            data[key] = value

    safe = True if hasattr(kwargs, 'safe') and kwargs.safe else False
    kwargs['safe'] = safe

    # Delete kwargs message, data, additionalFields
    try:
        if 'message' in kwargs:
            del kwargs['message']
        if 'additionalFields' in kwargs:
            del kwargs['additionalFields']

    except ValueError:
        pass

    # Now check for any model and convert them to dict
    # Or extract their keys if kwargs['extract_key'] is true
    extract_key = False
    if 'extract_key' in kwargs:
        extract_key = kwargs['extract_key']
        del kwargs['extract_key']

    data = serialize(data, extract_key) if not raw else data

    return JsonResponse(data, *args, **kwargs)


def successJson(data: object = {}, *args, **kwargs):
    """Send Json API success

    Keyword Arguments:
        data object -- The data to send back (default: {})

    Returns:
        HttpResponse -- Django HttpResponse
    """
    response = {
        'success': True,
        'message': kwargs.get('message') or 'Success'
    }

    if data:
        response['data'] = data

    return json(response, *args, **kwargs)


def failJson(data: object = {}, *args, **kwargs):
    """Send Json API Failure

    Keyword Arguments:
        data object -- The data to send back (default: {})

    Returns:
        HttpResponse -- Django HttpResponse
    """
    response = {
        'success': False,
        'message': kwargs.get('message') or 'Error',
    }

    if data:
        response['data'] = data

    return json(response, status=400, *args, **kwargs)


def renderOrFail(template: str, request: HttpRequest, context: object = {}, *args, **kwargs) -> HttpResponse:
    """
    Render a django template if it exist or return to 404 page

    :param str template: The template to render
    :param HttpResponse request: The request object
    :param object content: Data to send along with the template (default {})

    :rtype: HttpResponse
    :raises Http404: if the template is not found
    """
    try:
        loadTemplate = get_template(template)
    except TemplateDoesNotExist:
        # return render404(request)
        raise Http404
    else:
        return HttpResponse(loadTemplate.render(context=context, request=request), *args, **kwargs)


def render(*args, **kwargs):
    '''
    An alias to renderOrFail
    '''
    return renderOrFail(*args, **kwargs)


def render404(request):
    '''
    Render the 404 page
    '''
    return renderOrFail('web/404.html', request, {}, status=404)


def request(url: str, params: dict = {}, method: str = 'GET'):
    """Make an http request

    Arguments:
        url {str} -- The endpoint url

    Keyword Arguments:
        params {dict} -- request body (default: {{}})
        method {str} -- request method, POST, GET, PUT, DELETE (default: {'GET'})

    Raises:
        Exception: Unknown request method

    Returns:
        string -- JSON Response
    """

    if method.upper() not in ('GET', 'POST', 'PUT', 'DELETE'):
        raise Exception('Error: Unknown request method')
    return getattr(requests, method.lower())(url, **params)


def get_json(url: str, params: dict = {}):
    """Get remote JSON using the request method

    Arguments:
        url {str} -- The request url

    Keyword Arguments:
        params {dict} -- request body (default: {{}})

    Returns:
        string -- JSON String
    """
    response = requests.get(url, params)
    if str(response.status_code).startswith('20'):
        return response.json()
    return None


def download_remote_file(url: str, filename: str = None):
    """Download a remote file

    Arguments:
        url {str} -- The request url

    Keyword Arguments:
        filename {str} -- Filename to save the file as (default: {None})

    """
    try:
        file = urlretrieve(url, filename)
        return file
    except Exception:
        return False


def download_remote_image(url: str):
    """Download remote image and process with Pillow

    Arguments:
        url {str} -- The request url

    Returns:
        [PIL.Image] -- Pillow Image
    """

    image = download_remote_file(url, path.join(
        gettempdir(), f"{randomStringDigits()}.jpg"))
    try:
        im = Image.open(image[0])
        # is it valid?
        im.verify()
    except Exception:
        return False
    else:
        im = Image.open(image[0])
        return im
