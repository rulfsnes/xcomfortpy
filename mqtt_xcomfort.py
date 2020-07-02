#/usr/bin/env

#mqtt_xcomfort.py

import paho.mqtt.client as mqtt
import ctypes
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-mh", "--mqtt_host", metavar="--mqtt-host", type=str, help="enter mqtt host", nargs='?', default="localhost")

parser.add_argument("-n","--mqtt_name", metavar="--mqtt-name", type=str, help="enter mqtt host name", nargs='?', default="mqtt_xcomfort")

parser.add_argument("-c","--cdll", type=str, help="path to libxcomfort compiled and linked library", default="./libxcomfort.so", nargs='?')

requiredNamed = parser.add_argument_group('required named arguments')
parser.add_argument("-u","--user", type=str, help="enter mqtt user",nargs='?', required=True)

parser.add_argument("-P","--password", type=str, help="enter mqtt user pw", nargs='?', required=True)

args = parser.parse_args()


libxcomfort = ctypes.CDLL(args.cdll)

mqttClient = mqtt.Client(args.mqtt_name)
mqttClient.username_pw_set(username=args.user,password=args.password)


def on_message(client, userdata, msg):
    print("Message received: " + msg.topic +  " " + str(msg.payload))

def on_connect(client, userdata, flags, rc):
    print("Starting mqtt listening")
    client.subscribe("xcomfort/#")

mqttClient.on_message = on_message
mqttClient.on_connect = on_connect



mqttClient.connect(args.mqtt_host)
mqttClient.loop_forever()


