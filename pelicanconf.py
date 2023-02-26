AUTHOR = 'J. Vijn & gbadev.net community'
SITENAME = 'Tonc CE'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

THEME = 'theme'

STATIC_PATHS = ['img']

# use filenames for slug
SLUGIFY_SOURCE = 'basename'

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']

PLUGINS = [
  # 'headerid',
  'asciidoc3_reader',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True