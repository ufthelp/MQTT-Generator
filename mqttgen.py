#!/usr/bin/env python3
"""a simple sensor data generator that sends to an MQTT broker via paho"""
import json
import random
import timeit
import sys
import os
import json

import time

import threading
from threading import Thread
import paho.mqtt.client as mqtt

def generate(host, port, topic, sensors, message, interval,iThread):
    """generate data and send it to an MQTT broker"""
    mqttc = mqtt.Client()
    mqttc.connect(host, port)

    keys = list(sensors.keys())
    interval_secs = interval/ 1000.0
    loop = 0
    #Start timer
    start = timeit.default_timer()
    #iterate till the end last message
    while loop<(message):
        sensor_id = random.choice(keys)
        sensor = sensors[sensor_id]
        loop = loop + 1
        payload = json.dumps(sensor)

        #Uncomment this to check the sensor signals sent to broker
        # print("%s: %s" % (topic, payload))

        mqttc.publish(topic, payload)
        time.sleep(interval_secs)
    stop = timeit.default_timer()
    #Publish the execution time for pushing the data
    print("Thread" + str(iThread + 1) + "=" + str(round((message / (stop - start)), 2)) + "msg/sec")

def main(message,interval,iThread):
    """main entry point, load and validate config and call generate"""
    config_path = "config.json"
    try:
        with open(config_path) as handle:
            config = json.load(handle)
            mqtt_config = config.get("mqtt", {})
            sensors = config.get("sensors")

            if not sensors:
                print("no sensors specified in config.json")
                return

            host = mqtt_config.get("host", "localhost")
            port = mqtt_config.get("port", 1883)
            topic = mqtt_config.get("topic", "mqttgen")

            generate(host, port, topic, sensors,message, interval, iThread)
    except IOError as error:
        print("Error opening config file '%s'" % config_path, error)

if __name__ == '__main__':
    if len(sys.argv) == 4:
       #for multithreading
        for iThread in range(int(sys.argv[3])):
            Thread(target=main, args=(int(sys.argv[1]),int(sys.argv[2]),iThread)).start();
    else:
       print("Pass all the required parameters => mqttgen.py messageCounts messageInterval NoOfThread")
 
    # for iThread in range(5):
    #     Thread(target=main, args=(1, 0, iThread)).start();
