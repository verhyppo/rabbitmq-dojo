import unittest
import pika

class TestingClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.producer_credentials = pika.PlainCredentials("test_user", "test_user")
        producer_parameters = pika.ConnectionParameters(host="localhost",
                                       port=5672,
                                       virtual_host="test_vhost",
                                       credentials=self.producer_credentials,
                                       frame_max=10000)
        self.producer_connection = pika.BlockingConnection(producer_parameters)
        self.producer_channel = self.producer_connection.channel()

    def test_producerShouldCreateChannelWithNameQueue(self):
        self.producer_channel.queue_declare(queue="test.queue.1", durable=True)
        with self.assertRaises(Exception):
            self.producer_channel.queue_declare(queue="my_queue", durable=True)

    def test_producerProducesAndConsumerConsumes(self):
        self.producer_channel.basic_publish(exchange='test.exchange',
                      routing_key='test.rk',
                      body='Hello World!')
    
    @classmethod
    def tearDownClass(self):
        self.producer_connection.close()
if __name__ == '__main__':
    unittest.main()