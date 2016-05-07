import json
import logging
import logging.config
import os


def setup_logging(
        default_path='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(env_key, None)

    path = value if value else path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)