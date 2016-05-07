import json
import logging
import logging.config
import os


def setup_logging(
        path,
        default_file='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    # check if logs dir exists, if not, create it
    log_path = os.path.join(path, 'logs')
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    path = os.path.join(path, default_file)
    value = os.getenv(env_key, None)

    path = value if value else path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
