#!/usr/bin/python
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
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
    if message.topic == commandTopic:
        msgReceived = str(message.payload.decode("utf-8"))
        
        if msgReceived == "ON":
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(pin, GPIO.LOW)
            
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
