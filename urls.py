# coding: utf-8
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('ediary',
    url(r'^$', 'views.index', name='ediary-index'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)', 'views.article',
        name='ediary-article'),
    url(r'^draft/([0-9]+)', 'views.draft', name='ediary-draft'),
    url(r'^category/([^/]+)', 'views.category', name='ediary-category'),
    url(r'^tag/([^/]+)', 'views.tag', name='ediary-tag'),
    url(r'^feed', 'feed.handler', name='ediary-feed'),
)
