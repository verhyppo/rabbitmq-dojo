## Clustering

Create a 3 node cluster

1. start docker images
   ```
   docker network create test-rabbit
   docker run -d -v $HOME/.erlang.cookie:/var/lib/rabbitmq/.erlang.cookie -p 5672:5672 -p 15672:15672 -h rabbit1 --name rabbit1 --network test-rabbit rabbitmq
   docker run -d -v $HOME/.erlang.cookie:/var/lib/rabbitmq/.erlang.cookie -p 25672:5672 -p 35672:15672 -h rabbit2 --name rabbit2 --network test-rabbit rabbitmq
   docker run -d -v $HOME/.erlang.cookie:/var/lib/rabbitmq/.erlang.cookie -p 25673:5672 -p 35673:15672 -h rabbit3 --name rabbit3 --network test-rabbit rabbitmq
   ```
2. verify cluster status on all three nodes
   ```
   docker exec -it rabbit1 bash
   rabbitmqctl cluster_status
   docker exec -it rabbit2 bash
   rabbitmqctl cluster_status
   docker exec -it rabbit3 bash
   rabbitmqctl cluster_status
   ```
3. create a cluster between node 1 and 2 
   ```
   docker exec -it rabbit2 bash
   rabbitmqctl stop_app
   rabbitmqctl reset
   rabbitmqctl join_cluster rabbit@rabbit1
   rabbitmqctl start_app
   ```
4. allow data collection on all nodes
   ```
   rabbitmq-plugins enable rabbitmq_management_agent
   ```
   reload console on node1 so that all the nodes statistics are updated
5. join node 3 with node 2 (no matter the nodes)
   ```
   docker exec -it rabbit3 bash
   rabbitmqctl stop_app
   rabbitmqctl reset
   rabbitmqctl join_cluster rabbit@rabbit2
   rabbitmqctl start_app
   rabbitmq-plugins enable rabbitmq_management_agent
   ```
open console from both server to see what happened
6. create a queue and apply policy for ha
   ```
   ./rabbitmqadmin -u guest -p guest declare queue name=test.queue
   ./rabbitmqadmin -u guest -p guest declare exchange name=test.exchange type=direct
   ./rabbitmqadmin -u guest -p guest declare binding source=test.exchange destination=test.queue routing_key=test.rk
   rabbitmqctl set_policy --apply-to queues test.federation "^test\." '{"ha-mode":"all"}'
   ```
    