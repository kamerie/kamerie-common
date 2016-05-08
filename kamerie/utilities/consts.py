import os

# MQ

DISPATCHER_NAME = 'dispatcher'
EXCHANGE_NAME = 'kamerie-distribute'

# Type
TYPE_MOVIE = 'movie'
TYPE_SERIES = 'series'
TYPE_KEYS = [TYPE_SERIES, TYPE_MOVIE]

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
KAMERIE_LOGS_DIR = os.path.join(KAMERIE_CONFIG_DIR, 'logs')