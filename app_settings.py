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

from django.conf import settings

# General settings
EDIARY_TITLE = getattr(settings, 'EDIARY_TITLE', 'eDiary')
EDIARY_SUBTITLE = getattr(settings, 'EDIARY_SUBTITLE', 'yet another blog')
EDIARY_STYLE = getattr(settings, 'EDIARY_STYLE', 'default')
EDIARY_PAGINATEBY = getattr(settings, 'EDIARY_PAGINATEBY', 5)
EDIARY_DEFAULT_LANGUAGE = getattr(settings, 'EDIARY_DEFAULT_LANGUAGE', 'en')

# Use in page footer
EDIARY_COPYRIGHT_YEAR = getattr(settings, 'EDIARY_COPYRIGHT_YEAR', '2011')
EDIARY_COPYRIGHT = getattr(settings, 'EDIARY_COPYRIGHT', 'Igor Kalnitsky')
EDIARY_COPYRIGHT_URL = getattr(settings, 'EDIARY_COPYRIGHT_URL',
    'http://www.kalnitsky.org')
