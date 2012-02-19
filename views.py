# coding: utf-8
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from django.utils import translation

from utils import superuser_required, get_template_path, get_common_context
from ediary import app_settings
from models import Article, Category


def index(request, language=None):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return object_list(
        request,
        template_name=get_template_path('index.html'),
        queryset=Article.public.language(language).all(),
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
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=Article.public.language(language).filter(category=category),
        paginate_by=app_settings.EDIARY_PAGINATEBY,
        extra_context=dict(get_common_context(), **{'additional_title': slug}),
    )


def tag(request, slug, language="None"):
    language = language or app_settings.EDIARY_DEFAULT_LANGUAGE
    translation.activate(language)
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=Article.public.language(language).filter(tagline__icontains=slug),
        paginate_by=app_settings.EDIARY_PAGINATEBY,
        extra_context=dict(get_common_context(), **{'additional_title': slug}),
    )
