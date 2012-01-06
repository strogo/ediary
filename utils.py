# coding: utf-8
from django import http
from ediary import settings
from models import Category, NavigationLink, BlogrollItem


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


def get_common_context():
    return {
        'TITLE': settings.EDIARY_TITLE,
        'SUBTITLE': settings.EDIARY_SUBTITLE,
        'STYLE': settings.EDIARY_STYLE,
        'COPYRIGHT': settings.EDIARY_COPYRIGHT,
        'COPYRIGHT_URL': settings.EDIARY_COPYRIGHT_URL,

        'categories': Category.objects.all(),
        'navigation_links': NavigationLink.objects.all(),
        'blogroll_items': BlogrollItem.objects.all(),
    }
