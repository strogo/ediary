# coding: utf-8
from django.contrib import admin
from django import forms

from nani.admin import TranslatableAdmin
from nani.forms import TranslatableModelForm

from ediary import models


class ArticleAdmin(TranslatableAdmin):
    ordering = ['-published']
    list_filter = ['published']
    list_display = ['__unicode__', 'all_translations', 'published']
    search_fields = ['slug', 'title', 'pk']
    fields = ['slug', 'title', 'text', 'tagline', 'category', 'published',
              'allow_comments']

    class form(TranslatableModelForm):
        class Meta:
            model = models.Article
            widgets = {
                'slug': forms.TextInput(attrs={'size': 80}),
                'title': forms.TextInput(attrs={'size': 80}),
                'text': forms.Textarea(attrs={'cols': 80, 'rows': 30}),
                'tags': forms.TextInput(attrs={'size': 80}),
            }


class CategoryAdmin(TranslatableAdmin):
    list_display = ['__unicode__', 'all_translations']
    fields = ['slug', 'title', 'description']

    class form(TranslatableModelForm):
        class Meta:
            model = models.Category

class NavigationLinkAdmin(TranslatableAdmin):
    list_display = ['__unicode__', 'all_translations']
    fields = ['url', 'title', 'description']

    class form(TranslatableModelForm):
        class Meta:
            model = models.NavigationLink


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.NavigationLink, NavigationLinkAdmin)
