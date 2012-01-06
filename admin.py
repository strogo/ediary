# coding: utf-8
from django.contrib import admin
from django import forms

from ediary import models


class ArticleAdmin(admin.ModelAdmin):
    ordering = ['-published']
    list_filter = ['published']
    list_display = ['title', 'category', 'published']
    search_fields = ['slug', 'title', 'pk']
    fields = ['slug', 'title', 'text', 'tagline', 'category', 'published',
              'allow_comments']

    class form(forms.ModelForm):
        class Meta:
            model = models.Article
            widgets = {
                'slug': forms.TextInput(attrs={'size': 80}),
                'title': forms.TextInput(attrs={'size': 80}),
                'text': forms.Textarea(attrs={'cols': 80, 'rows': 30}),
                'tags': forms.TextInput(attrs={'size': 80}),
            }


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, list_display=['title', 'description'])
admin.site.register(models.NavigationLink,
    list_display=['title', 'description', 'url'])
admin.site.register(models.BlogrollItem,
    list_display=['title', 'description', 'url'])
