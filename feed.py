# coding: utf-8
from django.contrib.syndication.views import Feed
from django.db import models
from django.utils import translation

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
        return Article.public.language(translation.get_language())[:10]

    def item_link(self, item):
        return item.get_absolute_url()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html()

    def item_pubdate(self, item):
        return item.published


def handler(request, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return RssArticleFeed()(request)
