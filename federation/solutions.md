## Federation Plugin


downstream receives from upstream messages
rabbit1 downstream
rabbit2 upstream

1. start docker images
   ```
   docker network create test-rabbit
   docker run -d -v $HOME/.erlang.cookie:/var/lib/rabbitmq/.erlang.cookie -p 5672:5672 -p 15672:15672 -h rabbit1 --name rabbit1 --network test-rabbit rabbitmq
   docker run -d -v $HOME/.erlang.cookie:/var/lib/rabbitmq/.erlang.cookie -p 25672:5672 -p 35672:15672 -h rabbit2 --name rabbit2 --network test-rabbit rabbitmq
   ```
2. enable federation plugin from rabbit-cli container
   ```
   docker exec -it rabbit1 bash
   rabbitmq-plugins enable rabbitmq_federation rabbitmq_management rabbitmq_federation_management
   docker exec -it rabbit2 bash
   rabbitmq-plugins enable rabbitmq_federation rabbitmq_management rabbitmq_federation_management
   ```
3. configure federation 
   ```
   rabbitmqctl set_parameter federation-upstream test.upstream '{"uri":"amqp://rabbit2","expires":3600000}'
   rabbitmqctl set_policy --apply-to exchanges test.federation "^test\." '{"federation-upstream":"test.upstream"}'
   ```
4. create exchange, queue and binding that matches the federation pattern on the downstream server
   ```
   ./rabbitmqadmin -u guest -p guest declare queue name=test.queue
   ./rabbitmqadmin -u guest -p guest declare exchange name=test.exchange type=direct
   ./rabbitmqadmin -u guest -p guest --vhost test_vhost declare binding source=test.exchange destination=test.queue routing_key=test.rk
   ```
open console from both server to see what happened
send a message in rabbit 2 to queue test.exchange, check if it has been forwarder to 1

    