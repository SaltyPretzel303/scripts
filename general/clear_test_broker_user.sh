#!/bin/bash

# replace with the name of your docker container hosting rabbitmq
container="gg-broker"

docker exec $container rabbitmqctl delete_user test_user
docker exec $container rabbitmqctl delete_vhost test_vhost

