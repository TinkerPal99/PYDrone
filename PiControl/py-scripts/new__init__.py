# coding=utf-8
#! usr/bin/env/python

import RPi.GPIO as GPIO
from myLib import lib_gy521, class_PiControl
import urllib
import time

PiControl = class_PiControl.PiControl("http://192.168.8.200/main/")

while True:

    PiControl.gyro_CallOnRead(PiControl.gyro_read())
    time.sleep(0.2)
