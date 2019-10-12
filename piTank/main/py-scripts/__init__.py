#! usr/bin/env/python
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import time
from threading import Thread
import RPi.GPIO as GPIO
from myLib import lib_distance, lib_movement, lib_HTTP_Interface

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

enableA = 36
enableB = 32

port1 = 40
port2 = 38
port3 = 35
port4 = 37
lampA = 33
lampB = 31

GPIO.setup(enableA, GPIO.OUT)  # EnA
GPIO.setup(enableB, GPIO.OUT)  # EnB

GPIO.setup(port1, GPIO.OUT)  # 1
GPIO.setup(port2, GPIO.OUT)  # 2
GPIO.setup(port3, GPIO.OUT)  # 3
GPIO.setup(port4, GPIO.OUT)  # 4

GPIO.setup(lampA, GPIO.OUT)
GPIO.setup(lampB, GPIO.OUT)

# set speed; max = 100 min = 16
start_dc = 100
cont_dc = 50
# Defining pwm
wheelright_pwm = GPIO.PWM(enableA, 100)
wheelleft_pwm = GPIO.PWM(enableB, 100)


def clean():
    GPIO.output(port1, GPIO.LOW)
    GPIO.output(port2, GPIO.LOW)
    GPIO.output(port3, GPIO.LOW)
    GPIO.output(port4, GPIO.LOW)

    GPIO.output(lampA, GPIO.LOW)
    GPIO.output(lampB, GPIO.LOW)
    return



#####################################################################################################################
#################################################_________Hauptprogramm_____________#################################
#####################################################################################################################
#print("main")
wheelright_pwm.start(start_dc)
wheelleft_pwm.start(start_dc)

while True:
    # Datei oeffnen zum lesen, dies jedesmal zu Beginn der Schleife um auf Veraenderungen zu reagieren
    f = open("../test.txt", "r")
    lines = f.readlines()
    f.close()
    time.sleep(0.5)
    #print("while")
    try:
	#print ("try")
        #datei oeffnen zum bearbeiten
	for line in lines:
            f = open("../test.txt", "w")

            if "RPS1" in line:
                print ("Move forward")
                lib_movement.wheel_right_FORWARD(lampB, port1, port2)
                lib_movement.wheel_left_FORWARD(lampB, port3, port4)
            elif "RPS2" in line:
                print("Disabled  drive")
                lib_movement.clean(lampA, lampB, port1, port2, port3, port4)
            elif "RPS3" in line:
                print("Taking right")
                lib_movement.wheel_right_FORWARD(lampB, port1, port2)
                lib_movement.wheel_left_BACKWARD(lampA, port3, port4)
                time.sleep(0.6)
                lib_movement.clean(lampA, lampB, port1, port2, port3, port4)
            elif "RPS4" in line:
                print("Taking left")
                lib_movement.wheel_left_FORWARD(lampA, port3, port4)
                lib_movement.wheel_right_BACKWARD(lampB, port1, port2)
                time.sleep(0.6)
                lib_movement.clean(lampA, lampB, port1, port2, port3, port4)
            elif "RPS5" in line:
                print ("Moving backward")
                lib_movement.wheel_left_BACKWARD(lampA, port3, port4)
                lib_movement.wheel_right_BACKWARD(lampB, port1, port2)
            elif "RPS6" in line:
                print ("Half Speed")
                wheelleft_pwm.ChangeDutyCycle(cont_dc)
                wheelright_pwm.ChangeDutyCycle(cont_dc)
            elif "RPS7" in line:
                print ("Full Speed")
                wheelright_pwm.ChangeDutyCycle(start_dc)
                wheelleft_pwm.ChangeDutyCycle(start_dc)
            elif "RHF" in line:
                ()
            elif "LLL" in line:
                ()
            else:
                print ("Disabled")
                f.write(line)
            time.sleep(0.1)
            f.close()
    except KeyboardInterrupt:
        # User pressed CTRL-C
        # Reset GPIO settings
        lib_movement.clean(enableA, port1, port2, enableB, port3, port4)
        wheelleft_pwm.stop()
        wheelright_pwm.stop()
        break

