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
3. enable management create a cluster among all three nodes
   ```
   docker exec -it rabbit1 bash
   rabbitmq-plugins enable rabbitmq_management
   rabbitmqctl -n rabbit@rabbit2 stop_app
   rabbitmqctl -n rabbit@rabbit2 join_cluster rabbit@rabbit1
   rabbitmqctl -n rabbit@rabbit2 start_app
   rabbitmqctl -n rabbit@rabbit3 stop_app
   rabbitmqctl -n rabbit@rabbit3 join_cluster rabbit@rabbit1
   rabbitmqctl -n rabbit@rabbit3 start_app
   ```
4. enable management
   ```
    docker exec -it rabbit2 bash
    rabbitmq-plugins enable rabbitmq_management   
    docker exec -it rabbit3 bash
    rabbitmq-plugins enable rabbitmq_management   
   ```
   reload console on node1 so that all the nodes statistics are updated
5. create a queue and apply policy for quorum queues
   ```
   ./rabbitmqadmin -u guest -p guest declare queue name=test.queue arguments='{"x-queue-type":"quorum"}'
   ./rabbitmqadmin -u guest -p guest declare exchange name=test.exchange type=direct
   ./rabbitmqadmin -u guest -p guest declare binding source=test.exchange destination=test.queue routing_key=test.rk
   rabbitmqctl set_policy --apply-to queues test.federation "^test\." '{"ha-mode":"all"}'
   ```
6. verify quorum and remove node
   ```
   rabbitmq-queues quorum_status test.queue
   rabbitmq-queues delete_member test.queue rabbit@rabbit1
   rabbitmq-queues quorum_status test.queue
   ```
7. readd member
   ```
   rabbitmq-queues add_member test.queue rabbit@rabbit1
   rabbitmq-queues quorum_status test.queue
   ```
    