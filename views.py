# coding: utf-8
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from utils import superuser_required, get_template_path
from ediary import settings
from models import Article, Category, NavigationLink, BlogrollItem


DEFAULT_CONTEXT = {
    'TITLE': settings.EDIARY_TITLE,
    'SUBTITLE': settings.EDIARY_SUBTITLE,
    'STYLE': settings.EDIARY_STYLE,
    'COPYRIGHT': settings.EDIARY_COPYRIGHT,
    'COPYRIGHT_URL': settings.EDIARY_COPYRIGHT_URL,

    'categories': Category.objects.all(),
    'navigation_links': NavigationLink.objects.all(),
    'blogroll_items': BlogrollItem.objects.all(),
}


def index(request):
    return object_list(
        request,
        template_name=get_template_path('index.html'),
        queryset=Article.public.all(),
        paginate_by=settings.EDIARY_PAGINATEBY,
        extra_context=DEFAULT_CONTEXT,
    )


def article(request, year, month, day, slug):
    return render_to_response(
        get_template_path('article.html'),
        {'article': get_object_or_404(Article, slug=slug)},
        context_instance=RequestContext(request, DEFAULT_CONTEXT)
    )


@superuser_required
def draft(request, pk):
    return render_to_response(request, 'article.html', {
        'article': get_object_or_404(Article, pk=pk),
    })


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=Article.public.filter(category=category),
        paginate_by=settings.EDIARY_PAGINATEBY,
        extra_context=dict(DEFAULT_CONTEXT, **{'additional_title': slug}),
    )


def tag(request, slug):
    return object_list(
        request,
        template_name=get_template_path('list.html'),
        queryset=Article.public.filter(tagline__icontains=slug),
        paginate_by=settings.EDIARY_PAGINATEBY,
        extra_context=dict(DEFAULT_CONTEXT, **{'additional_title': slug}),
    )
