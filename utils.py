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
from models import Category, NavigationLink

from django import http


def superuser_required(func):
    def wrapper(req, *args, **kwargs):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        if not req.user.is_authenticated() or not req.user.is_superuser:
            return http.HttpResponseForbidden('Superuser required')
        return func(req, *args, **kwargs)
    return wrapper


def get_template_path(template_name):
    return 'ediary/{0}/{1}'.format(app_settings.EDIARY_STYLE, template_name)


def get_common_context():
    return {
        'TITLE': app_settings.EDIARY_TITLE,
        'SUBTITLE': app_settings.EDIARY_SUBTITLE,
        'STYLE': app_settings.EDIARY_STYLE,
        'COPYRIGHT': app_settings.EDIARY_COPYRIGHT,
        'COPYRIGHT_URL': app_settings.EDIARY_COPYRIGHT_URL,
        'COPYRIGHT_YEAR': app_settings.EDIARY_COPYRIGHT_YEAR,
        'DEFAULT_LANGUAGE': app_settings.EDIARY_DEFAULT_LANGUAGE,

        'categories': Category.objects.all(),
        'navigation_links': NavigationLink.objects.all(),
    }
