# coding: utf-8
from django.contrib.sitemaps import Sitemap
from models import Article


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Article.public.all()

    def lastmod(self, item):
        return item.updated
