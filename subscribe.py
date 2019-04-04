#!/usr/bin/python
import paho.mqtt.client as mqtt
import RPi._GPIO as gpio
import time
import os
import datetime

thingid = os.getenv('thingid','actor')
brokeraddr = os.getenv('brokeraddr','openhabian')
pin = int(os.getenv('pin', '17'))

thingTopic = "jumajumo/" + thingid + "/"
commandTopic = thingTopic + "command"

def on_connect(client, userdata, flags, rc):
    client.subscribe(commandTopic, qos=1)
    
def on_message(client, userdata, message):

   if str(message.topic) == str(commandTopic):
      msgReceived = str(message.payload)
        
      if str(message.payload) == str("ON"):
         gpio.output(pin, 1)
         time.sleep(1)
         gpio.output(pin, 0)
            
         client.publish(commandTopic, "OFF", qos=1, retain=True)

client = mqtt.Client(thingid)

client.will_set(thingTopic, "undef", qos=1, retain=True)
client.on_connect=on_connect
client.on_message=on_message 

client.connect(brokeraddr)

client.publish(thingTopic, str(datetime.datetime.now()), qos=1, retain=True)
client.publish(thingTopic + "sys/type", "actor", qos=1, retain=True)
client.publish(thingTopic + "sys/device", "relais-button", qos=1, retain=True)

client.loop_forever()
