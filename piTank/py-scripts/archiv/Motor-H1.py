# coding=utf-8
## @package archive
# Documentation for this module.

#! usr/bin/env/python
import time
from threading import Thread
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT) #EnA
GPIO.setup(32, GPIO.OUT) #EnB

GPIO.setup(40, GPIO.OUT) #1
GPIO.setup(38, GPIO.OUT) #2
GPIO.setup(35, GPIO.OUT) #3
GPIO.setup(37, GPIO.OUT) #4

GPIO.setup(33, GPIO.OUT) #Lights
GPIO.setup(31, GPIO.OUT) #Lights

speed = 0
en = "null"

def enable(en):

   if en == A:
      GPIO.output(36, GPIO.HIGH)
   if en == B:
      GPIO.output(32, GPIO.HIGH)
   if en == AB:
      GPIO.output(32, GPIO.HIGH)
      GPIO.output(36, GPIO.HIGH)
   return

def disable(en):

   if en == A:
      GPIO.output(36, GPIO.LOW)
   if en == B:
      GPIO.output(32, GPIO.LOW)
   if en == AB:
      GPIO.output(32, GPIO.LOW)
      GPIO.output(36, GPIO.LOW)
   return

def wheelleft_FORWARD():
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.LOW)

    GPIO.output(33, GPIO.HIGH)
    return

def wheelleft_BACKWARD():
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.HIGH)

    GPIO.output(33, GPIO.HIGH)
    return

def wheelright_FORWARD():
    GPIO.output(40, GPIO.HIGH)
    GPIO.output(38, GPIO.LOW)

    GPIO.output(31, GPIO.HIGH)
    return

def wheelright_BACKWARD():
    GPIO.output(40, GPIO.LOW)
    GPIO.output(38, GPIO.HIGH)

    GPIO.output(31, GPIO.HIGH)
    return

def speed():
    while 1:
       if speed == 1:
          enable(A)
          enable(B)
          time.sleep(0.05)
          disable(A)
          disable(B)
       if speed == 2:
          enable(A)
	  enable(B)
    return

def clean():
    GPIO.output(36, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)

    GPIO.output(40, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    GPIO.output(33, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
    return

def main():
#Datei oeffnen zum lesen, dies jedesmal zu Beginn der Schleife um auf Veraenderungen zu reagieren
	f = open("../test.txt", "r")

	lines = f.readlines()
	f.close

	time.sleep(0.5);
#Datei oeffnen zum bearbeiten

	for line in lines:
		f = open("../test.txt", "w")
		if speed == 1:
		
	        if "RPS1" in line:
			print "Move forward"
			wheelright_FORWARD()
			wheelleft_FORWARD()
      		elif "RPS2" in line:
			print "Disabled  drive";
			speed = 0;
			clean()
		elif "RPS3" in line:
			print "Taking right";
			wheelright_FORWARD()
			wheelleft_BACKWARD()
			time.sleep(0.4)
			clean()
		elif "RPS4" in line:
			print "Taking left";
			wheelleft_FORWARD()
			wheelright_BACKWARD()
			time.sleep(0.4)
			clean()
		elif "RPS5" in line:
			print "Moving backward";
			wheelleft_BACKWARD()
			wheelright_BACKWARD()

                if "RPS6" in line:
                        print "Half Speed";
			speed =1
		elif "RPS7" in line:
			print "Full Speed"
			speed =2
       		elif "RHF" in line:
			()
		elif "LLL" in line:
			()
		else:
			print "Disabled"
			f.write(line)
			#time.sleep(0.1)
	f.close

while 1:
	main()
