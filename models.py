# coding: utf-8
from django.db import models
from nani.models import TranslatableModel, TranslationManager, TranslatedFields
from django.utils import translation
from django.utils.translation import ugettext as _

from ediary import app_settings


class Category(TranslatableModel):
    slug = models.SlugField(max_length=200, unique=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=255, blank=True),
        description = models.TextField(blank=True),
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

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
    def get_query_set(self):
        qs = super(self.__class__, self).get_query_set()
        return qs.exclude(published=None)

    def language(self, language=None):
        return super(self.__class__, self).language(language).order_by('-published')


class Article(TranslatableModel):
    slug = models.SlugField(max_length=200, unique=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=255, blank=True),
        text = models.TextField(blank=True),
    )

    tagline = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category)
    published = models.DateTimeField(blank=True, null=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(blank=True, default=True)

    objects = TranslationManager()
    public = PublicArticlesManager()

    def __unicode__(self):
        return self.safe_translation_getter('title', self.slug)

    @models.permalink
    def get_absolute_url(self):
        args = [
            '{:04d}'.format(self.published.year),
            '{:02d}'.format(self.published.month),
            '{:02d}'.format(self.published.day),
            self.slug,
        ]

        language = translation.get_language()
        if language != app_settings.EDIARY_DEFAULT_LANGUAGE:
            args.append(language)

        if self.published:
            return ('ediary-article', args)
        return ('ediary-draft', [str(self.pk), language])


    def tags(self):
        return [tag.lstrip() for tag in self.tagline.split(',')]

    def intro(self):
        import re
        pattern = re.compile(r'(.*)..\s+readmore.*', re.S)
        intro = re.match(pattern, self.text)
        if intro:
            print intro.groups
            return intro.groups(0)[0]
        else:
            return self.text[:300]


class NavigationLink(TranslatableModel):
    url = models.URLField()

    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.CharField(max_length=255, blank=True),
    )

    def __unicode__(self):
        return self.safe_translation_getter('title', self.url)

