#! usr/bin/env/python
import time
import RPi.GPIO as GPIO

from PiTank import PiTank
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

GPIO_TRIGGER = 1
GPIO_ECHO = 1

distance_forward = 10
########################################################################################################################
##################################################__Setting Object__####################################################
########################################################################################################################

PiTank.__init__(PiTank, enableA, enableB, 100, port1, port2, port3, port4)
PiTank.set_lamp(PiTank, lampA, lampB)
PiTank.set_Forward_Sensor(PiTank, GPIO_TRIGGER, GPIO_ECHO)

print ("pins declared as ")
PiTank.print_motor_h(PiTank)
PiTank.print_Sensor(PiTank)

########################################################################################################################
#################################################_Start_of_Main#########################################################
########################################################################################################################
while True:
    try:
        while lib_distance.measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO) >= 40:
            PiTank.start_pwm(PiTank, 100)
            PiTank.vehicle_drive(PiTank, "forward")
        if lib_distance.measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO) <= 40:
            PiTank.change_pwm(PiTank, 50, 35)
        elif lib_distance.measure_average_of_x(5, GPIO_TRIGGER, GPIO_ECHO) <= 10:
            PiTank.vehicle_drive(PiTank, "stop")
            PiTank.vehicle_drive(PiTank, "rightturn")
            time.sleep(0.5)
            PiTank.vehicle_drive(PiTank, "stop")

    except KeyboardInterrupt:
        lib_movement.clean(lampA, port1, port2, lampB, port3, port4)
        break;
