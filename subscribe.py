#!/usr/bin/python
import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import os
import datetime

thingid = os.getenv('thingid','actor')
brokeraddr = os.getenv('brokeraddr','openhabian')
pin = int(os.getenv('pin', '17'))

thingTopic = "jumajumo/" + thingid + "/"
commandTopic = thingTopic + "command"

ON=gpio.LOW
OFF=gpio.HIGH

gpio.setmode(gpio.BCM)
gpio.setup(pin,gpio.OUT)
gpio.output(pin,OFF)

def on_message(client, userdata, message):

   if message.topic == commandTopic:
      msgReceived = message.payload
      if "ON" == msgReceived.decode():
         gpio.output(pin,ON)
         time.sleep(1)
         gpio.output(pin,OFF)
         client.publish(commandTopic, "OFF")

client = mqtt.Client(thingid)

client.on_message=on_message

client.connect(brokeraddr)

client.subscribe(commandTopic)

client.publish(commandTopic, "ONLINE")
client.publish(thingTopic, str(datetime.datetime.now()), qos=1, retain=True)
client.publish(thingTopic + "sys/type", "actor", qos=1, retain=True)
client.publish(thingTopic + "sys/device", "relais-button", qos=1, retain=True)

client.loop_forever()

