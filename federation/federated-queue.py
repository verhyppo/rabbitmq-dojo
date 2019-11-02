import unittest
import pika

# send messages on the upstream and see that they are dequeued from the downstream
class TestingClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.consumer_credentials = pika.PlainCredentials("guest", "guest")

        consumer_parameters = pika.ConnectionParameters(host="localhost",
                                       port=5672,
                                       virtual_host="test_vhost",
                                       credentials=self.consumer_credentials,
                                       frame_max=10000)
        self.consumer_connection = pika.BlockingConnection(consumer_parameters)
        self.consumer_channel = self.consumer_connection.channel()

    def test_producerProducesAndConsumerConsumes(self):
        for method_frame, properties, body in self.consumer_connection.channel().consume(queue='test.queue', auto_ack=True):
            print(body)
            
    
    @classmethod
    def tearDownClass(self):
        self.consumer_connection.close()
if __name__ == '__main__':
    unittest.main()
