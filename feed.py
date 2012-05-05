# coding: utf-8

# Copyright 2011 Igor Kalnitsky <igor@kalnitsky.org>
#
# This file is part of eDiary.
#
# eDiary is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# eDiary is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with eDiary.  If not, see <http://www.gnu.org/licenses/>.

import app_settings
from models import Article

from django.contrib.syndication.views import Feed
from django.db.models import permalink
from django.utils import translation
from django.template import Template, Context


class RssArticleFeed(Feed):
    title = app_settings.EDIARY_TITLE
    description = app_settings.EDIARY_SUBTITLE

    year = app_settings.EDIARY_COPYRIGHT_YEAR
    author_name = app_settings.EDIARY_COPYRIGHT
    author_link = app_settings.EDIARY_COPYRIGHT_URL
    feed_copyright = u'© {} {}'.format(year, author_name)

    @permalink
    def link(self):
        return ('ediary-feed', [])

    def items(self):
        return Article.public.language(translation.get_language())[:10]

    def item_link(self, item):
        return item.get_absolute_url()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        t = Template('{% load markup %}{{ content|restructuredtext }}')
        return t.render(Context({'content': item.text}))

    def item_pubdate(self, item):
        return item.published


def handler(request, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return RssArticleFeed()(request)
