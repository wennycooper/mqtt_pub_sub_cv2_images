# Example for MQTT publishing and receiving cv2 images #

## Requirements ##
* Install mosquitto MQTT server 

    $ sudo apt-get install mosquitto
    
    (in ubuntu, it will start mosquitto service)

* Install MQTT python client "paho-mqtt"

    $ pip install paho-mqtt


## Run ##
* In terminal1

    $ python ./sub.py

* In terminal2

    $ python ./pub.py



