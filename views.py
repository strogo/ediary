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
from utils import superuser_required, get_template_path, get_common_context

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from django.utils import translation


def index(request, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    articles = Article.public.language(language).all()
    return object_list(
        request,
        template_name=get_template_path('index.html'),
        queryset=articles.prefetch_related('category'),
        paginate_by=app_settings.EDIARY_PAGINATEBY,
        extra_context=get_common_context(),
    )


def article(request, year, month, day, slug, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return render_to_response(
        get_template_path('article.html'),
        {'article': get_object_or_404(Article, slug=slug)},
        context_instance=RequestContext(request, get_common_context())
    )


@superuser_required
def draft(request, pk, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return render_to_response(
        get_template_path('article.html'),
        {'article': get_object_or_404(Article, pk=pk)},
        context_instance=RequestContext(request, get_common_context())
    )


def category(request, slug, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    category = get_object_or_404(Category, slug=slug)
    articles = Article.public.language(language).filter(category=category)
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=articles.prefetch_related('category'),
        paginate_by=app_settings.EDIARY_PAGINATEBY,
        extra_context=dict(get_common_context(), **{'additional_title': slug}),
    )


def tag(request, slug, language="None"):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    articles = Article.public.language(language).filter(tagline__icontains=slug)
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=articles.prefetch_related('category'),
        paginate_by=app_settings.EDIARY_PAGINATEBY,
        extra_context=dict(get_common_context(), **{'additional_title': slug}),
    )
