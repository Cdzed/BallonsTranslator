import os.path as osp

ICON_PATH = 'data/icons/[ICONNAME]'

UI_PATH = osp.dirname(osp.abspath(__file__))
PROGRAM_PATH = osp.dirname(UI_PATH)

LIBS_PATH = osp.join(PROGRAM_PATH, 'data/libs')

STYLESHEET_PATH = osp.join(PROGRAM_PATH, 'data/config/stylesheet.css')
THEME_PATH = osp.join(PROGRAM_PATH, 'data/config/themes.json')
CONFIG_PATH = osp.join(PROGRAM_PATH, 'data/config/config.json')

CONFIG_FONTSIZE_HEADER = 18
CONFIG_FONTSIZE_TABLE = 14
CONFIG_FONTSIZE_CONTENT = 14

CONFIG_COMBOBOX_HEIGHT = 30 
CONFIG_COMBOBOX_SHORT = 200
CONFIG_COMBOBOX_MIDEAN = 332
CONFIG_COMBOBOX_LONG = 468

HORSLIDER_FIXHEIGHT = 36

WIDGET_SPACING_CLOSE = 8
TEXTEDIT_FIXWIDTH = 350

TEXTEFFECT_FIXWIDTH = 400
TEXTEFFECT_MAXHEIGHT = 500

LEFTBAR_WIDTH = 60
LEFTBTN_WIDTH = 38

LDPI = 96.
DPI = 188.75

DEFAULT_FONT_FAMILY = 'Microsoft YaHei UI'

WINDOW_BORDER_WIDTH = 4
BOTTOMBAR_HEIGHT = 32
TITLEBAR_HEIGHT = 30

PAGELIST_THUMBNAIL_MAXNUM = 100
PAGELIST_THUMBNAIL_SIZE = 48

FLAG_QT6 = False

SLIDERHANDLE_COLOR = (85,85,96)
FOREGROUND_FONTCOLOR = (93,93,95)