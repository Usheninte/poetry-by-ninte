#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Usheninte Dangana'
SITENAME = 'Poetry by Ninte'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Website', 'https://ninte.dev/'),
         ('Blog', 'https://blog.ninte.dev/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Usheninte'),
          ('LinkedIn', 'https://www.linkedin.com/in/usheninte/'),)

DEFAULT_PAGINATION = 42

DEFAULT_CATEGORY = 'Poetry'

# Extra cofigurations

RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False

STATIC_PATHS = [
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
