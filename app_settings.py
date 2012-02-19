# coding: utf-8
from django.conf import settings

# General settings
EDIARY_TITLE = getattr(settings, 'EDIARY_TITLE', 'eDiary')
EDIARY_SUBTITLE = getattr(settings, 'EDIARY_SUBTITLE', 'yet another blog')
EDIARY_STYLE = getattr(settings, 'EDIARY_STYLE', 'default')
EDIARY_PAGINATEBY = getattr(settings, 'EDIARY_PAGINATEBY', 5)
EDIARY_DEFAULT_LANGUAGE = getattr(settings, 'EDIARY_DEFAULT_LANGUAGE', 'en')

# Use in page footer
EDIARY_COPYRIGHT = getattr(settings, 'EDIARY_COPYRIGHT', 'Igor Kalnitsky')
EDIARY_COPYRIGHT_URL = getattr(settings, 'EDIARY_COPYRIGHT_URL',
    'http://www.kalnitsky.org')


# Use in feed
EDIARY_AUTHOR_NAME = getattr(settings, 'EDIARY_AUTHOR_NAME', 'Igor Kalnitsky')
EDIARY_AUTHOR_URL = getattr(settings, 'EDIARY_AUTHOR_URL',
    EDIARY_COPYRIGHT_URL)
EDIARY_AUTHOR_EMAIL = getattr(settings, 'EDIARY_AUTHOR_EMAIL',
    'igor@kalnitsky.org')
EDIARY_AUTHOR_COPYRIGHT = getattr(settings, 'EDIARY_AUTHOR_COPYRIGHT',
    '© 2012 Igor Kalnitsky')
