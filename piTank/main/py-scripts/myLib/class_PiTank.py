# coding=utf-8
## @package Libraries
# Documentation for this module.

#! usr/bin/env/python
from myLib import lib_movement
import RPi.GPIO as GPIO

class PiTank:
    enableA = 1
    enableB = 1
    port1 = 1
    port2 = 1
    port3 = 1
    port4 = 1

    lampA = 1
    lampB = 1

    GPIO_TRIGGER_FORWARD = 1
    GPIO_ECHO_FORWARD = 1

    GPIO_ECHO_BACKWARD = 1
    GPIO_TRIGGER_BACKWARD = 1

    def __init__(self, enableA, enableB, maximum_pulse, port1, port2, port3, port4):
        self.wheelleft_pwm = GPIO.PWM(enableB, maximum_pulse)
        self.wheelright_pwm = GPIO.PWM(enableA, maximum_pulse)
        self.enableA = enableA
        self.enableB = enableB
        self.port1 = port1
        self.port2 = port2
        self.port3 = port3
        self.port4 = port4

    def set_lamp(self, lampA, lampB):
        self.lampA = lampA
        self.lampB = lampB

    def set_Forward_Sensor(self, GPIO_TRIGGER, GPIO_ECHO):
        self.GPIO_TRIGGER_FORWARD = GPIO_TRIGGER
        self.GPIO_ECHO_FORWARD = GPIO_ECHO

    def set_Backward_Sensor(self, GPIO_TRIGGER, GPIO_ECHO):
        self.GPIO_TRIGGER_BACKWARD = GPIO_TRIGGER
        self.GPIO_ECHO_BACKWARD = GPIO_ECHO

    def print_Sensor(self):
        print("GPIO_TRIGGER_FORWARD" + str(self.GPIO_TRIGGER_FORWARD))
        print("GPIO_ECHO_FORWARD" + str(self.GPIO_ECHO_FORWARD))
        print("GPIO_TRIGGER_BACKWARD" + str(self.GPIO_TRIGGER_BACKWARD))
        print("GPIO_ECHO_BACKWARD" + str(self.GPIO_ECHO_BACKWARD))

    def print_motor_h(self):
        print("enableA" + str(self.enableA))
        print("enableB" + str(self.enableB))
        print("port1" + str(self.port1))
        print("port2" + str(self.port2))
        print("port3" + str(self.port3))
        print("port4" + str(self.port4))
        print("lampA" + str(self.lampA))
        print("lampB" + str(self.lampB))

    def vehicle_drive(self, direction):
        """

        :type direction: string forward, backward, stop, leftturn, rightturn
        """
        if direction == "forward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_FORWARD(self.lampA, self.port3, self.port4)
        elif direction == "backward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_BACKWARD(self.lampA, self.port3, self.port4)
        elif direction == "stop":
            lib_movement.clean(self.lampA, self.port1, self.port2, self.lampB, self.port3, self.port4)
            #print ("Stopped")
        elif direction == "leftturn":
            lib_movement.wheel_left_BACKWARD(self.lampA, self.port3, self.port4)
            lib_movement.wheel_right_FORWARD(self.lampB, self.port1, self.port2)
        elif direction == "rightturn":
            lib_movement.wheel_left_FORWARD(self.lampA, self.port3, self.port4)
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
        else:
            print ("Wrong input")

    def start_pwm(self, startpulse):
        self.wheelright_pwm.start(startpulse)
        self.wheelleft_pwm.start(startpulse)

    def change_pwm(self, changepulse_right, changepulse_left):
        self.wheelleft_pwm.ChangeDutyCycle(changepulse_left)
        self.wheelright_pwm.ChangeDutyCycle(changepulse_right)

    def stop_pwm(self):
        self.wheelleft_pwm.stop()
        self.wheelright_pwm.stop()
