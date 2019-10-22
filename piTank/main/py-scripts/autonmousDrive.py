#! usr/bin/env/python
import time
import RPi.GPIO as GPIO

from myLib.class_PiTank import (PiTank)
from myLib import lib_distance, lib_movement

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

GPIO_TRIGGER = 16
GPIO_ECHO = 18

distance_forward = 10


#################################################_Setup_###############################################################
GPIO.setup(enableA, GPIO.OUT)  # EnA
GPIO.setup(enableB, GPIO.OUT)  # EnB

GPIO.setup(port1, GPIO.OUT)  # 1
GPIO.setup(port2, GPIO.OUT)  # 2
GPIO.setup(port3, GPIO.OUT)  # 3
GPIO.setup(port4, GPIO.OUT)  # 4

GPIO.setup(lampA, GPIO.OUT)
GPIO.setup(lampB, GPIO.OUT)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
########################################################################################################################
##################################################__Setting Object__####################################################
########################################################################################################################

piTank = PiTank(enableA, enableB, 100, port1, port2, port3, port4)
#PiTank.__init__(piTank, enableA, enableB, 100, port1, port2, port3, port4)
PiTank.set_lamp(piTank, lampA, lampB)
PiTank.set_Forward_Sensor(piTank, GPIO_TRIGGER, GPIO_ECHO)

print ("pins declared as ")
PiTank.print_motor_h(piTank)
PiTank.print_Sensor(piTank)

########################################################################################################################
#################################################_Start_of_Main#########################################################
########################################################################################################################
try:
    while True:
        print("Try")
	distance = int(lib_distance.measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO))
	print (distance)
        if lib_distance.measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO) >= 40:
           PiTank.start_pwm(piTank, 100)
           PiTank.vehicle_drive(piTank, "forward")
           print("forward")
        elif lib_distance.measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO) < 40:
            PiTank.change_pwm(piTank, 50, 35)
	    print("slight right avoid")
        else:
	#elif lib_distance.measure_average_of_x(5, GPIO_TRIGGER, GPIO_ECHO) <= 10:
            PiTank.change_pwm(piTank, 70, 70)
	    PiTank.vehicle_drive(piTank, "stop")
            PiTank.vehicle_drive(piTank, "rightturn")
            time.sleep(0.5)
            PiTank.vehicle_drive(piTank, "stop")
	    print("rightturn")
	time.sleep(0.5)
#        lib_movement.clean(lampA, port1, port2, lampB, port3, port4)


except KeyboardInterrupt:
   lib_movement.clean(lampA, port1, port2, lampB, port3, port4)
