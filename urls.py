# coding: utf-8
from django.conf.urls.defaults import patterns, url
from django.conf import settings

LANG_PATTERN = '|'.join([lang[0] for lang in settings.LANGUAGES])
LANG_PATTERN = '(?:({})/)?'.format(LANG_PATTERN)

urlpatterns = patterns('ediary',
    url(r'^{}$'.format(LANG_PATTERN), 'views.index', name='ediary-index'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/' + '{}$'.format(LANG_PATTERN),
        'views.article', name='ediary-article'),
    url(r'^draft/(\d+)/{}$'.format(LANG_PATTERN), 'views.draft',
        name='ediary-draft'),
    url(r'^category/([^/]+)/{}$'.format(LANG_PATTERN), 'views.category',
        name='ediary-category'),
    url(r'^tag/([^/]+)/{}$'.format(LANG_PATTERN), 'views.tag',
        name='ediary-tag'),
    url(r'^feed/{}$'.format(LANG_PATTERN), 'feed.handler',
        name='ediary-feed'),
)
