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

import models

from nani.admin import TranslatableAdmin
from nani.forms import TranslatableModelForm

from django.contrib import admin
from django import forms


class ArticleAdmin(TranslatableAdmin):
    '''
        TODO: - add model title to ordering
              - add model title to search fields
              - show category title
    '''

    ordering = ['-published', 'category']
    list_filter = ['category', 'published', 'updated']
    list_display = ['__unicode__', 'category', 'all_translations', 'published']
    search_fields = ['slug', 'category', 'pk']
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
