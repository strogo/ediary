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

import app_settings

from nani.models import TranslatableModel, TranslationManager, TranslatedFields

from django.db import models
from django.utils import translation
from django.utils.translation import ugettext as _

import re


class Category(TranslatableModel):
    slug = models.SlugField(max_length=255, unique=True,
            verbose_name=_(u'Slug'))

    translations = TranslatedFields(
        title = models.CharField(max_length=255, blank=True,
            verbose_name=_(u'Title')),
        description = models.TextField(blank=True,
            verbose_name=_(u'Description')),
    )

    class Meta:
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')

    def __unicode__(self):
        return self.safe_translation_getter('title', self.slug)

    @models.permalink
    def get_absolute_url(self):
        args = [self.slug, ]
        language = translation.get_language()
        if language != app_settings.EDIARY_DEFAULT_LANGUAGE:
            args.append(language)
        return ('ediary-category', args)


class PublicArticlesManager(TranslationManager):

    @staticmethod
    def public(qs):
        return qs.exclude(published=None).order_by('-published')

    def get_query_set(self):
        return self.public(super(self.__class__, self).get_query_set())

    def language(self, language=None):
        return self.public(super(self.__class__, self).language(language))


class Article(TranslatableModel):
    slug = models.SlugField(max_length=200, unique=True,
            verbose_name=_(u'Slug'))

    translations = TranslatedFields(
        title = models.CharField(max_length=255, blank=True,
            verbose_name=_(u'Title')),
        text = models.TextField(blank=True, verbose_name=_(u'Text')),
    )

    tagline = models.CharField(max_length=255, blank=True,
            verbose_name=_(u'Tags'))
    category = models.ForeignKey(Category, verbose_name=_(u'Category'))
    published = models.DateTimeField(blank=True, null=True, db_index=True,
            verbose_name=_(u'Published'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_(u'Updated'))
    allow_comments = models.BooleanField(blank=True, default=True,
            verbose_name=_(u'Allow comments'))

    objects = TranslationManager()
    public = PublicArticlesManager()

    class Meta:
        verbose_name = _(u'Article')
        verbose_name_plural = _(u'Articles')

    def __unicode__(self):
        return self.safe_translation_getter('title', self.slug)

    @models.permalink
    def get_absolute_url(self):
        language = translation.get_language()
        if not self.published:
            return ('ediary-draft', [str(self.pk), language])

        args = [
            '{:04d}'.format(self.published.year),
            '{:02d}'.format(self.published.month),
            '{:02d}'.format(self.published.day),
            self.slug,
        ]

        if language != app_settings.EDIARY_DEFAULT_LANGUAGE:
            args.append(language)
        return ('ediary-article', args)

    def tags(self):
        return [tag.lstrip() for tag in self.tagline.split(',')]

    def intro(self):
        pattern = re.compile(r'(.*)\.\.\s+readmore.*', re.S)
        intro = re.match(pattern, self.text)
        return intro.groups(0)[0] if intro else self.text[:500]


class NavigationLink(TranslatableModel):
    url = models.URLField(verbose_name=_(u'URL'))

    translations = TranslatedFields(
        title = models.CharField(max_length=255,
            verbose_name=_(u'Title')),
        description = models.CharField(max_length=255,
            blank=True, verbose_name=_(u'Description')),
    )

    def __unicode__(self):
        return self.safe_translation_getter('title', self.url)
