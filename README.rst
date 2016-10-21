MQTT Generator
==============

A simple python 3 script to generate sensor data from a config file and send it
to an MQTT broker.

Usage
-----

The script uses the `python paho-mqtt library <https://pypi.python.org/pypi/paho-mqtt/>`_ you can install it with something like `sudo pip3 install paho-mqtt`.


Running:-
python mqttgen.py NoOfMessages Interval(ms) ThreadCount

Example:-
python mqttgen.py 1000 10 2

Configuration
-------------

Edit config.json, you can add as many sensors in the "sensors" object as you wish.
Change the host and topic details:-

 "host": "10.0.110.154"
  "topic": "sensor/70ff2d82-972e-11e6-8bde-4485001bc64b/data/test"
