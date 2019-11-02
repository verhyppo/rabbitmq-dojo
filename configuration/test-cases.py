import unittest
import pika

class TestingClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.consumer_credentials = pika.PlainCredentials("consumer", "password")

        consumer_parameters = pika.ConnectionParameters(host="localhost",
                                       port=5672,
                                       virtual_host="test_vhost",
                                       credentials=self.consumer_credentials,
                                       frame_max=10000)
        self.consumer_connection = pika.BlockingConnection(consumer_parameters)
        self.consumer_channel = self.consumer_connection.channel()


    def test_consumerCannotProduce(self):
        with self.assertRaises(Exception):
            self.consumer_channel.basic_publish(exchange='test.exchange',
                          routing_key='test.rk',
                          body='Hello World!')        

    def test_consumerShouldNotCreateQueue(self):
        with self.assertRaises(Exception):
            self.consumer_channel.queue_declare(queue="queue", durable=True)

    def test_producerProducesAndConsumerConsumes(self):
        for method_frame, properties, body in self.consumer_connection.channel().consume(queue='test.queue', auto_ack=True):
            self.assertEquals(body, "Hello World!")
            break
    
    @classmethod
    def tearDownClass(self):
        self.consumer_connection.close()
if __name__ == '__main__':
    unittest.main()