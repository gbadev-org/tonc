import sys
sys.path.append('.')
from extensions.xnos import XNosExtension

AUTHOR = 'J. Vijn & gbadev.net community'
SITENAME = 'Tonc'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Don't put pages in a subdirectory
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

DISPLAY_PAGES_ON_MENU = False

MARKDOWN = {
  'extensions': [
    'fenced_code',
    'toc',
    'attr_list',
    'md_in_html',
    'codehilite',
    XNosExtension(),
  ],
  'extension_configs': {
    'markdown.extensions.toc': {
      'anchorlink': True,
      'toc_depth': '2-2',
    },
  },
}

PAGE_LIST = [
  {
    'name': "Preface",
    'pages': [
      ('i', 'toc', "Contents"),
      ('ii', 'intro', "Introduction to Tonc"),
    ]
  }, {
    'name': "GBA Basics",
    'pages': [
      ('1', 'hardware', "GBA Hardware"),
      ('2', 'setup', "Setting up a development environment"),
      ('3', 'first', "My First GBA Demo"),
      ('4', 'video', "Video Introduction"),
      ('5', 'bitmaps', "The bitmap modes"),
      ('6', 'keys', "The GBA keypad"),
      ('7', 'objbg', "Sprite and tiled background overview"),
      ('8', 'regobj', "Regular sprites"),
      ('9', 'regbg', "Regular tiled backgrounds"),
    ]
  }, {
    'name': "GBA Extended",
    'pages': [
      ('10', 'affine', "The affine transformation matrix"),
      ('11', 'affobj', "Affine sprites"),
      ('12', 'affbg', "Affine tiled backgrounds"),
      ('13', 'gfx', "Graphic effects"),
      ('14', 'dma', "Direct Memory Access"),
      ('15', 'timers', "Timers"),
      ('16', 'interrupts', "Hardware interrupts"),
      ('17', 'swi', "BIOS calls"),
      ('18', 'sndsqr', "Beep! GBA sound introduction"),
    ]
  }, {
    'name': "Advanced / Applications",
    'pages': [
      ('19', 'text', "Text systems"),
      ('20', 'mode7', "Mode 7"),
      ('21', 'mode7ex', "More Mode7 tricks"),
      ('22', 'tte', "Tonc's Text Engine"),
      ('23', 'asm', "Whirlwind tour of ARM assembly"),
      ('24', 'lab', "The Lab"),
    ]
  }, {
    'name': "Appendixes",
    'pages': [
      ('A', 'numbers', "Numbers, bits and bit operations"),
      ('B', 'fixed', "Fixed-point math & LUTs"),
      ('C', 'matrix', "Vector and matrix math"),
      ('D', 'makefile', "More on makefiles and compiler options"),
      ('E', 'edmake', "Make via editors"),
      ('F', 'refs', "References"),
      ('G', 'log', "Change Log"),
    ]
  }
]

# These aren't great but eh.

def prev_page(page):
  prev_num = None
  prev_slug = None
  prev_name = None
  for section in PAGE_LIST:
    for (num, slug, name) in section['pages']:
      if slug == page.slug:
        return (prev_num, prev_slug, prev_name)
      prev_num = num
      prev_slug = slug
      prev_name = name
  return (None, None, None)

def next_page(page):
  prev_slug = None
  for section in PAGE_LIST:
    for (num, slug, name) in section['pages']:
      if prev_slug == page.slug:
        return (num, slug, name)
      prev_slug = slug
  return (None, None, None)

# Make these utilities available in page template.
PREV = prev_page
NEXT = next_page


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
PLUGINS = []

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
DIRECT_TEMPLATES = ['index']
