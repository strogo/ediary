# coding: utf-8
from django.contrib.syndication.views import Feed
from django.http import HttpResponseRedirect
from django.db import models

from models import Article
from ediary import app_settings


class RssArticleFeed(Feed):
    title = app_settings.EDIARY_TITLE
    description = app_settings.EDIARY_SUBTITLE

    author_name = app_settings.EDIARY_AUTHOR_NAME
    author_link = app_settings.EDIARY_AUTHOR_URL
    author_email = app_settings.EDIARY_AUTHOR_EMAIL
    feed_copyright = app_settings.EDIARY_AUTHOR_COPYRIGHT

    @models.permalink
    def link(self):
        return ('ediary-feed', [])

    def items(self):
        return Article.public.all()[:10]

    def item_link(self, item):
        return item.get_absolute_url()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html()

    def item_pubdate(self, item):
        return item.published


def handler(request):
    if app_settings.EDIARY_FEEDBURNER == '' or \
        request.META['HTTP_USER_AGENT'].startswith('FeedBurner'):
            return RssArticleFeed()(request)
    return HttpResponseRedirect(app_settings.EDIARY_FEEDBURNER)
