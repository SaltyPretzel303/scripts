#!/bin/bash

# replace with the name of your docker container hosting rabbitmq 
container="gg-broker"

docker exec $container rabbitmqctl add_user test_user test_pwd
docker exec $container rabbitmqctl add_vhost test_vhost
docker exec $container rabbitmqctl set_permissions -p test_vhost test_user ".*" ".*" ".*"
