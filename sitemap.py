# coding: utf-8
from django.contrib.sitemaps import Sitemap

from models import Article
from ediary import app_settings


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Article.public.language(app_settings.EDIARY_DEFAULT_LANGUAGE)

    def lastmod(self, item):
        return item.updated
