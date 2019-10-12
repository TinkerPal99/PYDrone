#! usr/bin/env/python
import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

counter = 0
a = "../Lizenzen/"

while 1:
    print os.listdir(a)
    time.sleep(0.5)

    while "Modul1.txt" in os.listdir(a):
        print "Modul 1, aktiv"
        time.sleep(120)

    while "Modul2.txt" in os.listdir(a):
        print "Modul 2, aktiv"
        time.sleep(120)
#Scheint dÃ¤mlich, oder ? Der folgende Abschnitt druckt einen Bescheid, dass keine aktive Lizenz besteht. Damit die Prompt aber nicht zugespammt wird, tut er dies nur alle 240000 Sekunden
    counter = counter + 1

    if counter == 200:
        print "No active License"
        counter = 0
