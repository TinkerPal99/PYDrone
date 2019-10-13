#! usr/bin/env/python
from myLib import lib_movement


class PiTank:
    enableA = 1
    enableB = 1
    port1 = 1
    port2 = 1
    port3 = 1
    port4 = 1

    lampA = 1
    lampB = 1

    def __init__(self, enableA, enableB, port1, port2, port3, port4):
        self.enableA = enableA
        self.enableB = enableB
        self.port1 = port1
        self.port2 = port2
        self.port3 = port3
        self.port4 = port4

    def set_lamp(self, lampA, lampB):
        self.lampA = lampA
        self.lampB = lampB

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
        if direction == "forward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_FORWARD(self.lampA, self.port3, self.port4)
        elif direction == "backward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_BACKWARD(self.lampA, self.port3, self.port4)
        else:
            print ("Wrong input")
