# coding=utf-8
## @package archive
# Documentation for this module.

#! usr/bin/env/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
counter = 0
a = "../Lizenzen/"
print (os.listdir(a))
while 1:
    print (os.listdir(a))
        time.sleep(0.5)
        while "Modul1.txt" in os.listdir(a):
            print ("Modul 1, aktiv")
        time.sleep(120)
        while "Modul2.txt" in os.listdir(a):
            print ("Modul 2, aktiv")
        time.sleep(120)

    counter = counter + 1

    if counter == 200:
        print ("No active License")
        counter = 0
