# [RABBITMQCTL](https://www.rabbitmq.com/rabbitmqctl.8.html)

[] start rabbitmq server
[] verify server up
[] restart nodes
[] change node name
[] create a new vhost `test_vhost`
[] create new user name: `test_user`, pwd: `test_user`
[] assign R/W to new vhost for the new user to create queue bindings and exchanges
[] list permissions
[] verify using rabbitmqctl-plugins if management plugin is active, if not active it.
[] create a new queue named `test.queue`
[] create a new exchange named `test.exchange`
[] create a new binding named `test.binding` that connects `test.exchange` to `test.queue` via `test.rk`
[] create new user name: `consumer`, pwd: `password`
[] allow the user to consume from queues
[] launch the test to see if it passes
