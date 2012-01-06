# coding: utf-8
from django import http
from ediary import settings


def superuser_required(func):
    def wrapper(req, *args, **kwargs):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        if not req.user.is_authenticated() or not req.user.is_superuser:
            return http.HttpResponseForbidden('Superuser required')
        return func(req, *args, **kwargs)
    return wrapper


def get_template_path(template_name):
    return 'ediary/{0}/{1}'.format(settings.EDIARY_STYLE, template_name)
