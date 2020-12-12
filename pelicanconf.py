#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Usheninte Dangana'
SITENAME = 'Poetry by Ninte'
SITEURL = 'https://poetry.ninte.dev'

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
LINKS = (('Website', 'https://ninte.dev/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Usheninte'),)

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'Poetry'

# Extra cofigurations

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
RELATIVE_URLS = True
