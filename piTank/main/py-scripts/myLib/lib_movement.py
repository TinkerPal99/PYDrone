#! usr/bin/env/python
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def wheel_left_FORWARD(lampA, port3, port4):
    GPIO.output(port3, GPIO.HIGH)
    GPIO.output(port4, GPIO.LOW)

    GPIO.output(lampA, GPIO.HIGH)
    return


def wheel_left_BACKWARD(lampA, port3, port4):
    GPIO.output(port3, GPIO.LOW)
    GPIO.output(port4, GPIO.HIGH)

    GPIO.output(lampA, GPIO.HIGH)
    return


def wheel_right_FORWARD(lampB, port1, port2):
    GPIO.output(port1, GPIO.HIGH)
    GPIO.output(port2, GPIO.LOW)

    GPIO.output(lampB, GPIO.HIGH)
    return


def wheel_right_BACKWARD(lampB, port1, port2):
    GPIO.output(port1, GPIO.LOW)
    GPIO.output(port2, GPIO.HIGH)

    GPIO.output(lampB, GPIO.HIGH)
    return


def clean(lampA, port1, port2, lampB, port3, port4):
    GPIO.output(lampA, GPIO.LOW)
    GPIO.output(lampB, GPIO.LOW)

    GPIO.output(port1, GPIO.LOW)
    GPIO.output(port2, GPIO.LOW)
    GPIO.output(port3, GPIO.LOW)
    GPIO.output(port4, GPIO.LOW)

    #GPIO.output(33, GPIO.LOW)
    #GPIO.output(31, GPIO.LOW)
    return




