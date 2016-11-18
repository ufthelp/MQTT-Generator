# MQTT-Generator
Test data MQTT generator acting as publisher of data to MQTT Broker(Listener) . Can be configured to generate multi threading interval base messages to mimic the behavior of Sensors in IOT.

Usage
-----

The script uses the `python paho-mqtt library <https://pypi.python.org/pypi/paho-mqtt/>`_ you can install it with something like `sudo pip3 install paho-mqtt`.


Running:-
python mqttgen.py NoOfMessages Interval(ms) ThreadCount

Example:-
python3 mqttgen.py 1000 10 2
python mqttgen.py 1000 10 2 (based on the python version)

Configuration
-------------

Edit config.json, you can add as many sensors in the "sensors" object as you wish.
Change the host and topic details:-

 "host": "10.0.110.154"
  "topic": "sensor/70ff2d82-972e-11e6-8bde-4485001bc64b/data/test
