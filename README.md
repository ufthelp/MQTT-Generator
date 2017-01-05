MQTT Data Generator
==============
Pre-requistes:-
1. Python (ubunto OS this is already installed)

2.The script uses the `python paho-mqtt library <https://pypi.python.org/pypi/paho-mqtt/>`_ you can install it with something like `sudo pip3 install paho-mqtt`.


Running:-
1.Browse to the generator location and type command in the terminal as below
	python3 mqttgen.py NoOfMessages Interval(ms) ThreadCount

Example:-
python3 mqttgen.py 1000 10 2

Configuration
-------------

Edit config.json, you can add as many sensors in the "sensors" object as you wish.

1.Change the host and topic details:-

 "host": IP
 "topic": "sensor/sensorID/data/Mapping Tag"

Example:-
 "host": "10.0.50.102"
 "topic": "sensor/45d24cfc-6c10-4e16-9beb-68186e31340a/data/Humidity"

2.Change the sensor as per the mapping
Example:- we had mapping of Key1 as Categorical and Key2 as Numerical 
    "sensors": {
        "Sensor 1": {
                "Key1":"Temp",
		"Key2": 30
		 }
      
    }
