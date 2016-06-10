import json
import logging
import logging.config
import os
import pkg_resources
from datetime import datetime

from kamerie.utilities.consts import KAMERIE_LOGS_DIR


def _setup_logging(name, default_file='logging.json', default_level=logging.INFO):
    # create logs directory (if not exists)
    logs_path = os.path.join(KAMERIE_LOGS_DIR, name)

    if not os.path.exists(logs_path) or not os.path.exists(logs_path):
        os.makedirs(logs_path)

    path = pkg_resources.resource_filename(__name__, default_file)

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)

        _setup_logger_files(config, 'file_handler', name)

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def _setup_logger_files(config, handler, name):
    if config.get('handlers', {}).get(handler, {}).get('filename', None):
        config['handlers'][handler]['filename'] = config['handlers'][handler]['filename'].format(
            name=name,
            path=os.path.join(KAMERIE_LOGS_DIR, name),
            timestamp='{:%Y-%m-%dT%H-%M-%S}'.format(datetime.now())
        )


def get_logger(name='plugin'):
    _setup_logging(name)
    logging.getLogger(name).info('Successfully initialized logger. Created log files in ~/.kamerie/logs')
    return logging.getLogger(name)


def list_plugins_from_repo(source):
    # from pkg_resources import resource_listdir as listdir
    # from pkg_resources import resource_isdir as isdir
    from os.path import isdir, join
    from os import listdir
    return filter(lambda p: isdir(join(source, p)) and p[0].isalnum(), listdir(source))


def get_plugin_requirements(plugin_path):
    from os.path import join, exists

    requirements_file = join(plugin_path, 'requirements.txt')
    libraries = []

    if exists(requirements_file):
        with open(requirements_file, 'r') as f:
            libraries += f.readlines()

    return list(set(libraries))
