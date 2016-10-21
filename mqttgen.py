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
    val = 0
    #Start timer
    start = timeit.default_timer()
    while val<(message):
        sensor_id = random.choice(keys)
        sensor = sensors[sensor_id]
        val = val + 1
        data = {
            "id": sensor_id,
            "value": val
        }
        #columns from json file
        for key in ["c1", "c2"]:
            value = sensor.get(key)

            if value is not None:
                data[key] = value

        payload = json.dumps(data)

        #Uncomment this to check the pushing to sensor signals
        #print("%s: %s" % (topic, payload))

        mqttc.publish(topic, payload)
        time.sleep(interval_secs)
    stop = timeit.default_timer()
    #Publish the execution time for pushing the data
    print("Thread" + str(iThread + 1) + "=" + str(round((message / (stop - start)), 2)) + "msg/sec")

def main(iThread,message,interval):
    """main entry point, load and validate config and call generate"""
    config_path = "config.json"
    try:
        with open(config_path) as handle:
            config = json.load(handle)
            mqtt_config = config.get("mqtt", {})
            sensors = config.get("sensors")

            if not sensors:
                print("no sensors specified in config, nothing to do")
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
            Thread(target=main(iThread,int(sys.argv[1]),int(sys.argv[2]))).start()
    else:
       print("Pass all the required parameters => mqttgen.py messageCounts messageInterval NoOfThread")
    # main(100000,1000,0)