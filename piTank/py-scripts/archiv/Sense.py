# coding=utf-8
## @package archive
# Documentation for this module.

#! usr/bin/env/python
from datetime import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
GPIO.setwarnings(False)

#Sensortyp (22/11) und Pin
sensor = Adafruit_DHT.DHT22
gpio = 4

#date

dateTimeObj = datetime.now()
datestamp = dateTimeObj.strftime("%Y-%m-%d")

#counter
h = 0
z = 0
e = 0

f = open("../senselog.txt", "a+")
f.write("---------------" + datestamp + "--------------------" +  "\n")
f.close()

#nummerizationcounter in das txt-log
while 1:

	e = e + 1
	if e == 10:
		e = 0
		z = z + 1
		if z == 10:
			z = 0
			h = h + 1
		else: ()
	else: ()
#datetime
	dateTimeObj = datetime.now()
	timestamp = dateTimeObj.strftime("(%H:%M)")


#Daten auslesen

	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

#Ausgabeaud CMD
	print timestamp + 'Temperatur: {0:0.1f}*C Luftfeuchtigkeit: {1:0.1f}%'.format(temperature,humidity)
#Ausgabe format in txt
	a =str(h)+str(z)+str(e) + "|" + timestamp + " | " + ' {0:0.1f}*C	 {1:0.1f}%'.format(temperature,humidity)
#Eingabe in das Senselog.txt

	f = open("../senselog.txt", "a+")

	for i in range (1):
		f.write(a + "\n")

	f.close()

	time.sleep(300)
