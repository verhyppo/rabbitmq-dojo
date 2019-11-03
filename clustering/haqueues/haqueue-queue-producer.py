import unittest
import pika

class TestingClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.producer_credentials = pika.PlainCredentials("guest", "guest")
        #produce on node 3
        producer_parameters = pika.ConnectionParameters(host="localhost",
                                       port=25673,
                                       credentials=self.producer_credentials,
                                       frame_max=10000)
        self.producer_connection = pika.BlockingConnection(producer_parameters)
        self.producer_channel = self.producer_connection.channel()

    def test_producerProducesAndConsumerConsumes(self):
        self.producer_channel.basic_publish(exchange='test.exchange',
                      routing_key='test.rk',
                      body='Hello World!')
        self.producer_channel.basic_publish(exchange='test.exchange',
                      routing_key='test.twonode',
                      body='Mirrored Queue with two nodes!')
    
    @classmethod
    def tearDownClass(self):
        self.producer_connection.close()
if __name__ == '__main__':
    unittest.main()