import os

# MQ
DISPATCHER_NAME = 'dispatcher'
EXCHANGE_NAME = 'kamerie-distribute'

# Type
TYPE_MOVIE = 'movie'
TYPE_SERIES = 'series'
TYPE_KEYS = [TYPE_SERIES, TYPE_MOVIE]
MEDIA_FILE_EXTENSIONS = ('.avi', '.mpg', '.mkv', '.mp4', '.m4p', \
                         '.flv', '.f4v', '.f4p', '.f4a', '.f4b', \
                         '.vob', '.ogv', '.ogg', '.mov', '.qt', \
                         '.3gp')

# Library
LIBRARY_PATH = 'library_path'
LIBRARY_TYPE = 'library_type'

# Media
MEDIA_TYPE = 'media_type'
MEDIA_PATH = 'media_path'
MEDIA_KEYS = [MEDIA_TYPE, MEDIA_PATH]

# Misc
SCANNED = 'scanned'

# File System
KAMERIE_HOME_DIR = os.path.expanduser("~")
KAMERIE_CONFIG_DIR = os.path.join(KAMERIE_HOME_DIR, '.kamerie')
KAMERIE_PLUGINS_DIR = os.path.join(KAMERIE_CONFIG_DIR, 'plugins')
KAMERIE_LOGS_DIR = os.path.join(KAMERIE_CONFIG_DIR, 'logs')
KAMERIE_PID_DIR = os.path.join(KAMERIE_CONFIG_DIR, 'pid')
DEFAULT_MAIN_MODULE = 'plugin.py'
DEFAULT_MAIN_CLASS = 'TemplatePlugin'
