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

    errors_log_path = os.path.join(logs_path, 'errors')
    info_log_path = os.path.join(logs_path, 'info')

    if not os.path.exists(errors_log_path) or not os.path.exists(info_log_path):
        os.makedirs(errors_log_path)
        os.makedirs(info_log_path)

    path = pkg_resources.resource_filename(__name__, default_file)

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)

        _setup_logger_files(config, 'error_file_handler', name)
        _setup_logger_files(config, 'info_file_handler', name)

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def _setup_logger_files(config, handler, name):
    if config.get('handlers', {}).get(handler, {}).get('filename', None):
        config['handlers'][handler]['filename'] = config['handlers'][handler]['filename'].format(
            path=os.path.join(KAMERIE_LOGS_DIR, name),
            timestamp='{:%Y-%m-%dT%H-%M-%S}'.format(datetime.now())
        )


def get_logger(name='plugin'):
    _setup_logging(name)
    logging.getLogger(name).info('Successfully initialized logger. Created log files in ~/.kamerie/logs')
    return logging.getLogger(name)
