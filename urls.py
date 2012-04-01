# coding: utf-8
'''
  Copyright 2011 Igor Kalnitsky <igor@kalnitsky.org>

  This file is part of eDiary.

  eDiary is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  eDiary is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with eDiary.  If not, see <http://www.gnu.org/licenses/>.
'''

import views, feed

from django.conf.urls.defaults import patterns, url
from django.conf import settings


LANG_PATTERN = '|'.join([lang[0] for lang in settings.LANGUAGES])
LANG_PATTERN = '(?:({})/)?'.format(LANG_PATTERN)


urlpatterns = patterns('',
    url(r'^{}$'.format(LANG_PATTERN), views.index, name='ediary-index'),
    url(r'^(\d{4})/(\d{2})/(\d{2})/([^/]+)/' + '{}$'.format(LANG_PATTERN),
        views.article, name='ediary-article'),
    url(r'^draft/(\d+)/{}$'.format(LANG_PATTERN), views.draft,
        name='ediary-draft'),
    url(r'^category/([^/]+)/{}$'.format(LANG_PATTERN), views.category,
        name='ediary-category'),
    url(r'^tag/([^/]+)/{}$'.format(LANG_PATTERN), views.tag,
        name='ediary-tag'),
    url(r'^feed/{}$'.format(LANG_PATTERN), feed.handler,
        name='ediary-feed'),
)
