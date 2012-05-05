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

import feed
from views import ShowIndex, ShowArticle, ShowDraft, ShowCategory, ShowTag

from django.conf.urls.defaults import patterns, url
from django.conf import settings


LANG_PATTERN = '|'.join([lang[0] for lang in settings.LANGUAGES])
LANG_PATTERN = '(?:(?P<language>{})/)?'.format(LANG_PATTERN)


urlpatterns = patterns('',
    # index page
    url(r'^{}$'.format(LANG_PATTERN), ShowIndex.as_view(),
        name='ediary-index'),

    # article
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[^/]+)/'
        + '{}$'.format(LANG_PATTERN), ShowArticle.as_view(),
        name='ediary-article'),
    url(r'^draft/(?P<pk>\d+)/{}$'.format(LANG_PATTERN), ShowDraft.as_view(),
        name='ediary-draft'),

    # category and tag
    url(r'^category/(?P<category>[^/]+)/{}$'.format(LANG_PATTERN),
        ShowCategory.as_view(), name='ediary-category'),
    url(r'^tag/(?P<tag>[^/]+)/{}$'.format(LANG_PATTERN),
        ShowTag.as_view(), name='ediary-tag'),

    # feed
    url(r'^feed/{}$'.format(LANG_PATTERN), feed.handler,
        name='ediary-feed'),
)
