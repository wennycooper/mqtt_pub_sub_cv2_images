import cv2
import paho.mqtt.client as mqtt
import time


mqttc = mqtt.Client("C1")
mqttc.connect("localhost", 1883, 60)

time.sleep(1)

cap = cv2.VideoCapture(0)
mqttc.loop_start()

while True:
    ret, frame = cap.read()
    #width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    #height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`

    #print(width, height)
    #cv2.imshow('video', frame)

    #cv2.waitKey(1)

    msg = frame.tobytes()

    i = mqttc.publish("mytopic", msg)
    i.wait_for_publish()

    




