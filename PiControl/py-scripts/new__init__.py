# coding=utf-8
# !usr/bin/env/python

import RPi.GPIO as GPIO
from myLib import lib_gy521, class_PiControl
import time

GPIO.setmode(GPIO.BOARD)

# --------------------------Preparation---------------------------------------------------------------------------------
piControl = class_PiControl.PiControl("http://192.168.8.200/main/", "/savings")

LAMP_Y = 1
LAMP_G = 1

Taster = 20
GPIO.setup(LAMP_Y, GPIO.IN)
GPIO.setup(LAMP_G, GPIO.IN)
# -----------------------------MAIN-------------------------------------------------------------------------------------
while True:
    if GPIO.input(Taster) == GPIO.HIGH:
        while True:
            piControl.gyro_CallOnRead(piControl.gyro_read())
            time.sleep(0.5)
            if GPIO.input(Taster) == GPIO.HIGH:
                GPIO.output(LAMP_Y) = GPIO.HIGH
                GPIO.output(LAMP_G) = GPIO.LOW
                time.sleep(5)
                break
    time.sleep(1)