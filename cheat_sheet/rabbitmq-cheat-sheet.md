## RabbitMQ cheat sheet
| reason            | command                                                           | meaning                                                                              |
|---|---|---|
| configure cluster | rabbitmqctl join_cluster {name}@{host} [--ram]                    | add this node to the cluster created by {host}                                       |
| monitoring        | rabbitmqctl cluster_status                                        | check cluster and node status                                                        |
| configure cluster | rabbitmqctl forget_cluster_node [--offline] {name}@{host}         | remove host from the cluster that contains this node                                 |
| maintanance       | rabbitmqctl force_boot                                            | force node boot reset all the data and cluster configurations                        |
| maintanance       | rabbitmqctl sync_queue [-p vhost] queue                           | force resync for a given queue. all consumers and producer are momemtarily stopped   |
| maintenance       | rabbitmqctl purge_queue [-p vhost] queue                          | purge all contents in a queue. in case of cluster queue all nodes queues are emptied |
| maintenance       | rabbitmqctl stop_app                                              | stop the application without killing Erlang VM                                       |
| maintenance       | rabbitmqctl start_app                                             | start the application after stop_app command has been issued                         |
| maintenance       | rabbitmqctl reset                                                 | reset the node. this command must be issued after stop_app                           |
| monitoring        | rabbitmqctl node_health_check                                     | runs a predefined list of healthcheck                                                |
| monitoring        | rabbitmqctl status                                                | comprehensive status of the current node                                             |
| maintenance       | rabbitmqctl list_*                                                | where * can be: queues, exchanges, bindings, connections, channels, consumer         |
| security          | rabbitmqctl add_user {username} {password}                        |                                                                                      |
| security          | rabbitmqctl delete_user {username}                                |                                                                                      |
| security          | rabbitmqctl change_password  {username} {new-pwd}                 |                                                                                      |
| security          | rabbitmqctl clear_password  {username}                            |                                                                                      |
| maintenance       | rabbitmqctl add_vhost {name}                                      |                                                                                      |
| maintenance       | rabbitmqctl list_vhosts                                           |                                                                                      |
| maintenance       | rabbitmqctl delete_vhost                                          |                                                                                      |
| security          | rabbitmqctl set_permissions -v {vhost} {username} conf write read | set permissions to a user. conf write and read are regexp                            |
| maintenance       | rabbitmq-plugins list                                             | list plugins                                                                         |
| maintenance       | rabbitmq-plugins enable {plugin name}                             | enable a plugin called {plugin name} and all of its dependencies                     |
| configuration     | rabbitmq-plugins set {plugin name}                                | enable {plugin name} and disable all the others                                      |
| monitoring| rabbitmq-diagnostics ping –q |check the server is up|
| monitoring| rabbitmq-diagnostics -q status |return a more comprehensive status of the server|
| monitoring| rabbitmq-diagnostics -q alarms |check alarm for partitions failure|
| monitoring| rabbitmq-diagnostics -q memory_breakdown --unit "MB" |breakdown memory usage by feature|
| monitoring| rabbitmq-diagnostics -q listeners |listening ports|
| monitoring| rabbitmq-diagnostics observer |lovely top-like app|