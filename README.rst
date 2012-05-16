###############################################################################
 eDiary
###############################################################################

=======
 About
=======

**eDiary** is an easy to use blog application for Django_. It was developed by
developer for developers.

The application supports all classic features:

- nice urls
- categories
- tags
- drafts (including post preview)
- code highlighting (works with docutils 0.9 and higher)
- reStructuredText markup language
- multilingual posts

Example: `www.kalnitsky.org`_


    NOTE: ``docutils 0.9`` is a current development version


==============
 Installation
==============

**eDiary** depends on two third-party libraries:

- ``pygments`` — used for code highlighting
- ``django-hvad`` — used for multilingual content

You should install these libraries before using project::

    $ sudo pip install pygments
    $ sudo pip install django_hvad

Then add ``eDiary`` application to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...

        'ediary',
    )


ake sure that ``INSTALLED_APPS`` also contains following items::

    INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',   # used for accessing static content
        'django.contrib.comments',      # used for adding comment system
        'django.contrib.sitemaps',      # used for generating sitemaps
        'django.contrib.markup',        # used for reST markup

        # ...

        'nani', # it's django-hvad
    )

Before using make sure that ``LANGUAGE_CODE`` is valid. The list of
valid values can be found in the ``LANGUAGES`` variable. By default
the following codes are valid::

    'ar' — Arabic
    'az' — Azerbaijani
    'bg' — Bulgarian
    'bn' — Bengali
    'bs' — Bosnian
    'ca' — Catalan
    'cs' — Czech
    'cy' — Welsh
    'da' — Danish
    'de' — German
    'el' — Greek
    'en' — English'
    'en-gb' — British English
    'eo' — Esperanto
    'es' — Spanish
    'es-ar' — Argentinian Spanish
    'es-mx' — Mexican Spanish
    'es-ni' — Nicaraguan Spanish
    'et' — Estonian
    'eu' — Basque
    'fa' — Persian
    'fi' — Finnish
    'fr' — French
    'fy-nl' — Frisian
    'ga' — Irish
    'gl' — Galician
    'he' — Hebrew
    'hi' — Hindi
    'hr' — Croatian
    'hu' — Hungarian
    'id' — Indonesian
    'is' — Icelandic
    'it' — Italian
    'ja' — Japanese
    'ka' — Georgian
    'kk' — Kazakh
    'km' — Khmer
    'kn' — Kannada
    'ko' — Korean
    'lt' — Lithuanian
    'lv' — Latvian
    'mk' — Macedonian
    'ml' — Malayalam
    'mn' — Mongolian
    'nb' — Norwegian Bokmal
    'ne' — Nepali
    'nl' — Dutch
    'nn' — Norwegian Nynorsk
    'pa' — Punjabi
    'pl' — Polish
    'pt' — Portuguese
    'pt-br' — Brazilian Portuguese
    'ro' — Romanian
    'ru' — Russian
    'sk' — Slovak
    'sl' — Slovenian
    'sq' — Albanian
    'sr' — Serbian
    'sr-latn' — Serbian Latin
    'sv' — Swedish
    'sw' — Swahili
    'ta' — Tamil
    'te' — Telugu
    'th' — Thai
    'tr' — Turkish
    'tt' — Tatar
    'uk' — Ukrainian
    'ur' — Urdu
    'vi' — Vietnamese
    'zh-cn' — Simplified Chinese
    'zh-tw' — Traditional Chines


=============
 Usage notes
=============

0. If eDiary finds ``.. readmore`` anywhere in the post it replaces last one
   with **readmore** link.

1. Set ``EDIARY_TITLE`` in ``settings.py`` for changing blog title.

2. Set ``EDIARY_SUBTITLE`` in ``settings.py`` for changing blog description.

3. Set ``EDIARY_STYLE`` in ``settings.py`` for changing blog style.

4. Set ``EDIARY_DEFAULT_LANGUAGE`` in ``settings.py`` for changing default
   language.

5. Set ``EDIARY_PAGINATEBY`` in ``settings.py`` for changing posts per page.

6. Set ``EDIARY_COPYRIGHT_YEAR`` in ``settings.py`` for changing copyright year
   in blog footer.

7. Set ``EDIARY_COPYRIGHT`` in ``settings.py`` for changing copyright text in
   blg footer.

8. Set ``EDIARY_COPYRIGHT_URL`` in ``settings.py`` for changing copyright url
   in blog footer.

============
 FAQ
============

0. **Why the reST markup language dosn't work?**

   Django reST filter depends on ``docutils`` project. So make sure that
   last one is installed in your system. ::

       $ sudo pip install docutils

1. **How to limit the list of available languages?**

   Just set ``LANGUAGES`` variable explicitly. For instance:::

       LANGUAGES = (
           ('en', _(u'Еnglish')),
           ('ru', _(u'Russian')),
       )

   It also removes the unnecessary language tabs from admin page.


.. _Django: http://www.djangoproject.com/
.. _`www.kalnitsky.org`: http://www.kalnitsky.org/blog/
