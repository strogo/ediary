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
from models import Article, Category
from utils import get_template_path, get_common_context

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.utils.decorators import method_decorator


class ArticlesList(ListView):
    ''' Show all available articles '''
    template_name = get_template_path('list.html')
    paginate_by = app_settings.EDIARY_PAGINATEBY
    context_object_name = 'article_list'
    allow_empty = False

    def get_queryset(self):
        lang = self.kwargs['language'] or app_settings.EDIARY_DEFAULT_LANGUAGE
        translation.activate(lang)
        qs = Article.public.language(lang).prefetch_related('category')
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        return dict(context, **get_common_context())


class ShowIndex(ArticlesList):
    ''' Show main page '''
    template_name = get_template_path('index.html')


class ShowCategory(ArticlesList):
    ''' Show articles from category '''

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category'])
        qs = super(ShowCategory, self).get_queryset()
        return qs.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(ShowCategory, self).get_context_data(**kwargs)
        context['additional_title'] = self.kwargs['category']
        return context


class ShowTag(ArticlesList):
    ''' Show articles with tag '''

    def get_queryset(self):
        qs = super(self.__class__, self).get_queryset()
        return qs.filter(tagline__icontains=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super(ShowTag, self).get_context_data(**kwargs)
        context['additional_title'] = self.kwargs['tag']
        return context


class ShowArticle(DetailView):
    ''' Show article '''
    template_name = get_template_path('article.html')
    context_object_name = 'article'
    model = Article

    def get_object(self):
        lang = self.kwargs['language'] or app_settings.EDIARY_DEFAULT_LANGUAGE
        translation.activate(lang)
        return super(ShowArticle, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data(**kwargs)
        context = dict(context, **get_common_context())
        return context


class ShowDraft(ShowArticle):
    ''' Show darft. Protect from guests. '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ShowDraft, self).dispatch(request, *args, **kwargs)
