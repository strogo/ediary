# coding: utf-8
from django.db import models
from markdown2 import markdown


class Category(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('ediary-category', [self.slug])


class PublicArticlesManager(models.Manager):
    def get_query_set(self):
        qs = super(self.__class__, self).get_query_set()
        return qs.exclude(published=None).order_by('-published')


class Article(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category)
    published = models.DateTimeField(blank=True, null=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(blank=True, default=True)

    objects = models.Manager()
    public = PublicArticlesManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        if self.published:
            return ('ediary-article', [
                '%04d' % self.published.year,
                '%02d' % self.published.month,
                '%02d' % self.published.day,
                '%s' % self.slug
            ])
        return ('ediary-draft', [str(self.pk)])

    def html(self):
        return markdown(self.text, True, extras=['code-color'])

    def tags(self):
        return [tag.lstrip() for tag in self.tagline.split(',')]

    def intro(self):
        import re
        pattern = re.compile(r'(.*)<!-- readmore -->.*', re.S)
        intro = re.match(pattern, self.html())
        if intro:
            print intro.groups
            return intro.groups(0)[0]
        else:
            return self.html()[:300]


class NavigationLink(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    url = models.URLField()

    def __unicode__(self):
        return self.title


class BlogrollItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    url = models.URLField()

    def __unicode__(self):
        return self.title
