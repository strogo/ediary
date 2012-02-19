# coding: utf-8
from django import template
from django.core.urlresolvers import reverse
from django.conf import settings

from ediary import app_settings


register = template.Library()


@register.filter(name='url_for_language')
def url_for_language(instance, language):
    """
        @TODO: REMOVE THIS FILTER IN FUTURE VERSIONS
    """
    args = [
        '{:04d}'.format(instance.published.year),
        '{:02d}'.format(instance.published.month),
        '{:02d}'.format(instance.published.day),
        instance.slug,
    ]

    if language != app_settings.EDIARY_DEFAULT_LANGUAGE:
        args.append(language)
    return reverse('ediary-article', args=args)

@register.filter(name='language_name')
def language_name(language_code):
    """
        @TODO: REMOVE THIS FILTER IN FUTURE VERSIONS
        USE {% get_language_info for LANGUAGE_CODE as lang %} instead
    """
    for code, name in settings.LANGUAGES:
        if code == language_code:
            return name.lower()
    return code
