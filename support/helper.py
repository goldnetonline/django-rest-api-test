'''
File: helper.py
Project: token-credit-backend
File Created: Tuesday, 4th February 2020 3:16:04 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Sunday, 25th October 2020 6:40:28 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''

from typing import Optional
import random
import string
from importlib import import_module
from django.db import models
from django.forms.models import model_to_dict
from django.utils.functional import LazyObject
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.template.exceptions import TemplateDoesNotExist
from django.utils.html import strip_tags
from django.core.mail import send_mail, mail_admins
from django.template import Template, Context
from .models import EmailTemplate


def config(key: str, default=None) -> Optional[str]:
    '''
    Read config from settings and return their value
    '''
    value = getattr(settings, key, None)
    return value if value is not None else default


def serialize(comp_obj: object, extract_key: bool = False):
    """Recursive convert complex object to serializable dictionary or simple primitive

    Args:
        comp_obj ([object]): Complex object
        extract_key (bool, optional): If to extract the key only if it is a model. Defaults to False.
    """
    def convert(value):
        from decimal import Decimal

        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        try:
            # print(type(value).mro())
            theMro = type(value).mro()
            if object in theMro:
                if models.base.Model in theMro or LazyObject in theMro:
                    if(extract_key):
                        return value.id if value.id else None
                    else:
                        theDict = model_to_dict(value)

                        # For some reasons inherited models dont serialize
                        # So add them here
                        additionals = [
                            'created_at', 'updated_at', 'slug'
                        ]
                        for added in additionals:
                            if(hasattr(value, added)):
                                theDict[added] = str(getattr(value, added))

                        if(hasattr(value.__class__, 'HIDDEN')):
                            try:
                                for hidden in value.__class__.HIDDEN:
                                    del theDict[hidden]
                            except Exception:
                                pass

                    return theDict
                elif Decimal in theMro:
                    return float(value)

                else:
                    print(type(value))
                    try:
                        return str(value)
                    except Exception:
                        return None
        except Exception:
            return value

    def recurse_dict(obj):
        if not isinstance(obj, dict):
            return convert(obj)
        for (k, v) in obj.items():
            if isinstance(v, (str, int, float, bool, )) or v is None:
                obj[k] = v
            elif isinstance(v, (dict, list, tuple)):
                obj[k] = recurse_dict(v)
            else:
                obj[k] = recurse_dict(convert(v))

        return obj

    return recurse_dict(comp_obj)


def randomStringDigits(length=6) -> str:
    """Generate a random string of letters and digits

    Keyword Arguments:
        length {int} -- Number of characters (default: {6})

    Returns:
        str -- Generated
    """

    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(length))


def getClassFromDotString(string: str):
    """
    Get a class from dot string notation
    like support.helper.someclass will return someclass with proper mro

    Arguments:
        string {str} -- The dot notation string

    Returns:
        Return a python class
    """

    moduleSplit = string.split('.')
    className = moduleSplit[-1]
    moduleName = ".".join(moduleSplit[:len(moduleSplit) - 1])
    module = import_module(moduleName)
    klass = getattr(module, className)
    return klass


def templateExists(template: str) -> bool:
    """
    Check if template exist

    Arguments:
        template {str} -- The template location

    Returns:
        bool -- Template exist or not
    """
    try:
        get_template(template)
    except TemplateDoesNotExist:
        raise False
    else:
        return True


def template2String(template: str, context: object = None) -> Optional[str]:
    """
    Compile a template to html string

    Arguments:
        template {str} -- The template location
        context {object} -- The context to pass along

    Returns:
        str -- The compiled string
    """
    try:
        return render_to_string(template, context)
    except TemplateDoesNotExist:
        return None


def html2PlainText(html: str) -> str:
    """
    Convert a html text to plain text

    Arguments:
        html {str} -- The html to convert

    Returns:
        [sre] -- The plain text string
    """
    return strip_tags(html)


def sendMail(template: str, subject: str, to: object, context: object = None, sender: str = None, **kwargs) -> bool:
    """
    A wrapper for send_mail
    Compile a template to html and string and send email

    Arguments:
        template {str} -- The template location
        subject {str} -- Mail Subject
        to {object} -- Mail recipients, can be string or list

    Keyword Arguments:
        context {object} -- The data to pass to the template (default: {None})
        sender {str} -- Opeional Sender (default: {None})

    Returns:
        bool -- send_mail 1 = sent and 0 not sent
    """

    html = template2String(template, context)
    text = html2PlainText(html)
    failMode = False

    if 'fail_silently' in kwargs:
        failMode = kwargs['fail_silently']
        del kwargs['fail_silently']

    if isinstance(to, str):
        to = [to]

    if not sender:
        sender = config('DEFAULT_FROM_EMAIL', 'noreply@server.com')
    try:
        send_mail(
            subject,
            text,
            sender,
            to,
            html_message=html,
            fail_silently=failMode,
        )
        return True
    except Exception:
        return False


def sendMailToAdmins(template: str, subject: str, context: object = None) -> bool:
    """
    A wrapper for mail_admins
    Compile a template to html and string and send email to site admin

    Arguments:
        template {str} -- The template location
        subject {str} --  The mail subject

    Keyword Arguments:
        context {object} -- The data to pass to the template  (default: {None})

    Returns:
        bool -- mail sent or not
    """

    html = template2String(template, context)
    text = html2PlainText(html)
    failMode = True

    try:
        mail_admins(
            subject,
            text,
            html_message=html,
            fail_silently=failMode,
        )
        return True
    except Exception:
        return False


def sendTemplateEmail(to: str, template: EmailTemplate, context: object = {}, **kwargs) -> bool:
    """
    Compile a string message from EmailTemplate and send email

    Arguments:
        to {str} -- The destination
        template {EmailTemplate} -- The template instance

    Keyword Arguments:
        context {object} -- Email message context (default: {{}})

    Returns:
        bool -- Mail sent or not
    """
    baseTemplate = config('EMAIL_BASE_LAYOUT', None)

    if not baseTemplate or not templateExists(baseTemplate):
        return False

    compiled = None
    try:
        compiled = Template(template.html_message)
        compiled = compiled.render(Context(context))
    except Exception:
        return False

    subject = None
    if 'subject' in kwargs:
        subject = kwargs['subject']
    else:
        subject = template.subject

    context.update({
        'main_message': compiled
    })

    return sendMail(baseTemplate, subject, to, context)


def json_encode(obj: dict) -> Optional[str]:
    """Encode a dict into JSON

    Args:
        obj (dict): The Object to Encode

    Returns:
        Optional[str]: JSON String
    """
    from json import dumps
    try:
        return dumps(obj)
    except Exception:
        return None


def json_decode(string: str) -> Optional[dict]:
    """Decode a dict into JSON

    Args:
        string (str): The string to Decode

    Returns:
        Optional[dict]: Dict obj
    """
    from json import loads
    try:
        return loads(string)
    except Exception:
        return None
