solution

start docker container
```
docker run -d --name rabbit rabbitmq
docker exec -it rabbit bash
```

1. `rabbitmq-server start &`
1. `rabbitmqctl status`
1. change node name + stop and start application 
    ```
    rabbitmqctl stop_app
    echo "NODENAME=hop-hop" > /etc/rabbitmq/rabbitmq-env.conf
    rabbitmqctl start_app
    rabbitmqctl status | grep -i "node name"
    ```
 
1. add new vhost 
  ```
  rabbitmqctl add_vhost test_vhost
  ```
1. add new user 
  ```
  rabbitmqctl add_user test_user test_user
  rabbitmqctl set_user_tags test_user administrator
  rabbitmqctl authenticate_user test_user test_user
  ```
1. set permissions write on queue and read on exchange in order to create new binding (see permission table)
  ```
  rabbitmqctl set_permissions --vhost test_vhost test_user "^test.*" "^test.queue$" "^test.exchange$"
  ```
2. verify permissions
  ```
  rabbitmqctl list_permissions --vhost test_vhost
  ```
1. create queue
  ```
  rabbitmq-plugins set rabbitmq_management
  curl localhost:15672/cli/rabbitmqadmin --output rabbitmqadmin
  chmod +x rabbitmqadmin
  ./rabbitmqadmin -u test_user -p test_user --vhost test_vhost declare queue name=test.queue
  ```
1. create exchange
  ```
  ./rabbitmqadmin -u test_user -p test_user --vhost test_vhost declare exchange name=test.exchange type=direct
  ```
1. create binding
   ```
   ./rabbitmqadmin -u test_user -p test_user --vhost test_vhost declare binding source=test.exchange destination=test.queue routing_key=test.rk
   ```
1. create consumer user
   ```
    rabbitmqctl add_user consumer password
    rabbitmqctl set_permissions --vhost test_vhost test_user "^$" "^$" "^test.queue$"
   ```
1. problem2 
   ```
   ./rabbitmqadmin export rabbit.definitions.json
   rabbitmqctl stop_app
   rabbitmqctl reset
   rabbitmqctl start_app
   ./rabbitmqadmin import rabbit.definitions.json
   ```

