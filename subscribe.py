#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
import os
import datetime

thingid = os.getenv('thingid','actor')
brokeraddr = os.getenv('brokeraddr','openhabian')
pin = int(os.getenv('pin', '17'))

thingTopic = "jumajumo/" + thingid + "/"
commandTopic = thingTopic + "command"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

client = mqtt.Client(thingid)

client.will_set(thingTopic, "undef", qos=1, retain=True)
client.on_message=on_message 

client.connect(brokeraddr)

client.publish(thingTopic, str(datetime.datetime.now()), qos=1, retain=True)
client.publish(thingTopic + "sys/type", "actor", qos=1, retain=True)
client.publish(thingTopic + "sys/device", "relais-button", qos=1, retain=True)

client.loop_start()

try:
    while True:

        client.subscribe(commandTopic, qos=1)
except:
    client.loop_stop() #stop the loop
    client.disconnect()
