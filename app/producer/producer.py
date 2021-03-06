import pika


def init_app(app):
    """Start Producer"""
    app.Producer = Producer(app)


class Producer:
    def __init__(self, app):
        self.app = app
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(app.config['RABBITMQ_HOST']))
        self.channel = self.connection.channel()

    def publish_data(self, message):
        """Publish the received data to the RabbitMQ queue"""
        self.channel.queue_declare(queue='send_message')
        self.channel.basic_publish(exchange='',
                                   routing_key='send_message',
                                   body=message
                                   )

    