import cv2
import paho.mqtt.client as mqtt
import time
import numpy as np

def on_message(client, userdata, message):
    y = np.frombuffer(message.payload, dtype=np.uint8)
    img = y.reshape(480, 640, 3)

    cv2.imshow('on_message_img', img)
    cv2.waitKey(1)


mqttc = mqtt.Client("C2")
mqttc.on_message = on_message
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("mytopic")

time.sleep(1)

mqttc.loop_forever()

