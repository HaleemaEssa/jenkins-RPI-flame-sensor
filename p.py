import RPi.GPIO as GPIO
import time
import pika
import random
import os
####flame-sensor ###
import adafruit_dht
from board import *
#GPIO SETUP
channel12 =12 #for flame
GPIO.setmode(GPIO.BCM)  
GPIO.setup(channel12, GPIO.IN)
credentials = pika.PlainCredentials('haleema', '4chyst')
parameters = pika.ConnectionParameters('192.168.0.126',
                                   5672,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
def callback2(channel12):
    if GPIO.input(channel12):
        return('0')
    else:
        return('1')
    return flame    #
    flame=0
GPIO.add_event_detect(channel12, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel12, callback2)  # assign function to GPIO PIN, Run function on change
def checkdht():
    for i in range(10):
        try:
            flame=callback2(channel12)
            message=str(flame)
            channel.basic_publish(exchange='logs', routing_key='', body= message)
            print ("sent %r" %message) 
        except RuntimeError:
            pass
        time.sleep(5)
while True:
    checkdht()
connection.close()
