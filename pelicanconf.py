AUTHOR = 'J. Vijn & gbadev.net community'
SITENAME = 'Tonc'
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

THEME = 'theme'

STATIC_PATHS = ['img']

# PAGE_URL = 'pages/{slug}.html'
# PAGE_URL = '{slug}.html'

# use filenames for slug
SLUGIFY_SOURCE = 'basename'

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['plugins']

PLUGINS = [
  'headerid',
  'asciidoc3_reader',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
DIRECT_TEMPLATES = ['index']
