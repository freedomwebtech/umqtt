import paho.mqtt.client as mqtt
import time


    
def on():
    mqttBroker ="broker.emqx.io"
    client = mqtt.Client("raspberry pi 400")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("LED on",'utf-8')))
    
    
on()    