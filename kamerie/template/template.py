import json
import os

import pika

from kamerie.utilities.consts import EXCHANGE_NAME, PACKAGE_JSON
from kamerie.utilities.utilities import get_logger


class TemplatePlugin(object):
    def __init__(self, plugin_name, path=None):
        # Prepare instance
        self.name = plugin_name
        self.path = os.getcwd() if not path else path
        self._load_credentials()

        # Connect to rabbitmq queue
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=EXCHANGE_NAME, type='direct')
        self._channel.queue_declare(queue=self.name)
        self._channel.queue_bind(queue=self.name, exchange=EXCHANGE_NAME, routing_key='')
        if self._logger:
            self._logger.info("Established %s's MQ connection" % self.name)

    def _load_credentials(self):
        package_json_path = os.path.join(self.path, PACKAGE_JSON) if not os.path.exists(PACKAGE_JSON) else PACKAGE_JSON
        if os.path.exists(package_json_path):
            with open(package_json_path) as f:
                package_info = json.load(f)

            self.__dict__.update(package_info)
            self._logger = get_logger(self.name)
            self._logger.info("Initializing {name}...".format(name=self.name))
            self._logger.info(json.dumps(package_info))
        else:
            self._logger.warning('no package file was found')

    def start(self):
        if self._logger:
            self._logger.info("Starting %s" % self.name)
        print "Starting %s" % self.name
        self._channel.basic_consume(self._message_received, queue=self.name, no_ack=True, exclusive=True)
        self._channel.start_consuming()

    def _message_received(self, channel, method, properties, message):
        message = json.loads(message)
        if self.name not in message.get('kamerie_plugins', []):
            self.on_message(message)

    def on_message(self, message):
        raise NotImplementedError("n00b")

    def send_message(self, message):
        pass
        # self._channel.basic_publish(exchange=self.rabbitmq_settings['exchange'],
        #                             routing_key=self.rabbitmq_settings['routing_key'],
        #                             body=message)

    def __exit__(self):
        self.close()

    def close(self):
        self._connection.close()
