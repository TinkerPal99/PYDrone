#! usr/bin/env/python
import time
#import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)

#first install "sudo pip install pyttsx"
import pyttsx

engine = pyttsx.init()
engine.say("First try")
engine.runAndWait()
