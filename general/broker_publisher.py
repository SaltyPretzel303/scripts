#!/usr/bin/python3

import signal  # used to trap SIGINT
import json  # used to parse and prettyPrint events
import sys
import pika  # rabbitmq client
from pika.credentials import PlainCredentials
import argparse  # util used to parse cli arguments
from os import environ  # used for reading environment variables

ENV_ADDRESS = 'BROKER_ADDRESS'
ENV_PORT = "BROKER_PORT"
ENV_V_HOST = "V_HOST"
ENV_TOPIC = "TARGET_TOPIC"

ENV_USERNAME = "BROKER_USERNAME"
ENV_PASSWORD = "BROKER_PASSWORD"

ENV_FILTER = "TARGET_FILTER"
DEFAULT_TOPIC = "random_topic"

DEFAULT_FILTER = ""  # todo check if this is actually allowed

DEFAULT_BROKER_ADDRESS = "127.0.0.1"
DEFAULT_BROKER_PORT = 5672
DEFAULT_BROKER_V_HOST = ""

DEFAULT_USERNAME = "guest"
DEFAULT_PASSWORD = "guest"

# region helper methods for resolving variables
# priority: env_variables -> cli_input -> default_values


def resolveAddress(cli_input):
    address = environ.get(ENV_ADDRESS)
    if(address is not None and address != ""):

        print("Using addres provided with ENV variable ... ")
        return address

    if (hasattr(cli_input, "broker_address") and
            (cli_input.broker_address is not None) and (cli_input.broker_address != "")):

        print("Using address provided with cli arg ... ")
        return cli_input.broker_address

    print("Using default address value: " + DEFAULT_BROKER_ADDRESS)
    return DEFAULT_BROKER_ADDRESS


def resolvePort(cli_input):
    port = environ.get(ENV_PORT)
    if(port is not None):

        print("Using port provided with ENV variable ... ")
        return port

    if (hasattr(cli_input, "broker_port") and
            (cli_input.broker_port is not None) and (cli_input.broker_port != "")):

        print("Using port provided with cli arg ... ")
        return cli_input.broker_port

    print("Using default port value: " + str(DEFAULT_BROKER_PORT))
    return DEFAULT_BROKER_PORT


def resolveVHost(cli_input):
    v_host = environ.get(ENV_V_HOST)
    if(v_host is not None):

        print("Using vHost provided with ENV varibale ... ")
        return v_host

    if(hasattr(cli_input, "vhost") and
       (cli_input.vhost is not None) and (cli_input.broker_port != "")):

        print("Using vhost provided with cli arg ... ")
        return cli_input.vhost

    print("Using default vhost value: " + DEFAULT_BROKER_V_HOST)
    return DEFAULT_BROKER_V_HOST


def resolveUsername(cli_input):
    username = environ.get(ENV_USERNAME)
    if (username is not None):
        print("Using username provided with ENV variable ... ")
        return username

    if (hasattr(cli_input, "username") and
            (cli_input.username is not None) and (cli_input.username != "")):

        print("Using username provided with cli arg ... ")
        return cli_input.username

    print("Using default username: " + DEFAULT_USERNAME)
    return DEFAULT_USERNAME


def resolvePassword(cli_input):
    password = environ.get(ENV_PASSWORD)
    if (password is not None):
        print("Using password provided with ENV variable ... ")
        return password

    if (hasattr(cli_input, "password") and
            (cli_input.password is not None) and (cli_input.password != "")):

        print("Using password provided with cli arg ... ")
        return cli_input.password

    print("Using default password: " + DEFAULT_PASSWORD)
    return DEFAULT_PASSWORD


def resolveTopic(cli_input):
    topic = environ.get(ENV_TOPIC)

    if (topic is not None):
        print("Using topic provided with ENV variable ... ")
        return topic

    if (hasattr(cli_input, "topic") and
            (cli_input.topic is not None) and (cli_input.password != "")):
        print("Using topic provided with cli arg ... ")
        return cli_input.topic

    print("Using default topic: " + DEFAULT_TOPIC)
    return DEFAULT_TOPIC


def resolveFilter(cli_input):
    filter = environ.get(ENV_FILTER)
    if(filter is not None):

        print("Using filter provided with ENV variable ... ")
        return filter

    if (hasattr(cli_input, "filter") and
            (cli_input.filter is not None) and (cli_input.filter != "")):

        print("Using filter provided with cli arg ... ")
        return cli_input.filter

    print("Using default filter:  " + DEFAULT_FILTER)
    return DEFAULT_FILTER


def resolveDat(cli_input):
    # data is required argument
    return cli_input.data

# endregion


parser = argparse.ArgumentParser(
        "Will publish data to specific topic with the specific filter \n\
	Default broker adress: localhost:5672\n")

# optional arguments
parser.add_argument("--address",
                    dest="broker_address",
                    required=False,
                    help="Message broker address. Default: localhost")

parser.add_argument("--port",
                    dest="broker_port",
                    required=False,
                    help="Message broker port. Default: 5672")

parser.add_argument("--vhost",
                    dest="vhost",
                    required=False,
                    help="Message broker virtual host. Default /")

parser.add_argument("--username",
                    dest="username",
                    required=False,
                    help="Username. Default 'guest'")

parser.add_argument("--password",
                    dest="password",
                    required=False,
                    help="Pasword. Default 'guest'")

parser.add_argument("--topic",
                    dest="topic",
                    help="Comma separated list of the topics to listen on. Default: topics from the soa project")

parser.add_argument("--filter",
                    dest="filter",
                    help="Filter to use on specified/all topics. Default: #")

parser.add_argument("--data",
                    dest="data",
                    required=True,
                    help="Data that is gonna be published.")

cli_input = parser.parse_args()

broker_address = resolveAddress(cli_input)
broker_port = resolvePort(cli_input)
broker_v_host = resolveVHost(cli_input)

username = resolveUsername(cli_input)
password = resolvePassword(cli_input)

print("")  # new line
print(f"Connecting with: {broker_address}:{broker_port}")
print("")  # new line

creds = PlainCredentials(username=username, password=password)
conn_params = pika.ConnectionParameters(host=broker_address,
                                        port=broker_port,
                                        virtual_host=broker_v_host,
                                        credentials=creds)

connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

topic = resolveTopic(cli_input)
filter = resolveFilter(cli_input)

data = cli_input.data

print("Publishing: " + data)
channel.basic_publish(topic, filter, data, None, False)
print("Data published ... ")

channel.close()
connection.close()
