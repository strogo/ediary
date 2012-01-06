# coding: utf-8
from django.contrib.syndication.views import Feed
from django.http import HttpResponseRedirect
from django.db import models

from models import Article
from ediary import settings


class RssArticleFeed(Feed):
    title = settings.EDIARY_TITLE
    description = settings.EDIARY_SUBTITLE

    author_name = settings.EDIARY_AUTHOR_NAME
    author_link = settings.EDIARY_AUTHOR_URL
    author_email = settings.EDIARY_AUTHOR_EMAIL
    feed_copyright = settings.EDIARY_AUTHOR_COPYRIGHT

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
    if settings.EDIARY_FEEDBURNER == '' or \
        request.META['HTTP_USER_AGENT'].startswith('FeedBurner'):
            return RssArticleFeed()(request)
    return HttpResponseRedirect(settings.EDIARY_FEEDBURNER)
