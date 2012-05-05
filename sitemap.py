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

from django.contrib.sitemaps import Sitemap
from django.utils import translation
from django.conf import settings


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def __init__(self, language=app_settings.EDIARY_DEFAULT_LANGUAGE):
        self.language = language

    def items(self):
        translation.activate(self.language)
        return Article.public.language(self.language).all()

    def lastmod(self, item):
        return item.updated


SITEMAP = {'ediary_{}'.format(code): ArticleSitemap(code) \
               for code, name in settings.LANGUAGES}
