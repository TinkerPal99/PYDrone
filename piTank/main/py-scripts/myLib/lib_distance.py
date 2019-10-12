#! usr/bin/env/python
from __future__ import print_function
import math
import time
import RPi.GPIO as GPIO

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Speed of sound in cm/s at temperature

temperature = 20
speedSound = 33100 + (0.6 * temperature)


def simple_measure(GPIO_TRIGGER, GPIO_ECHO):
    # Set pins as output and input
    global stop
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO, GPIO.IN)  # Echo
    # This function measures a distance
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    # Wait 10us
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    time.sleep
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()
        elapsed = stop - start
        distance = (elapsed * speedSound) / 2

    return distance


def measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO):
    # This function takes 3 measurements and
    # returns the average.

    distance1 = simple_measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance2 = simple_measure(GPIO_TRIGGER, GPIO_ECHO)
    time.sleep(0.1)
    distance3 = simple_measure(GPIO_TRIGGER, GPIO_ECHO)
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance


def measure_average_of_x(x, GPIO_TRIGGER, GPIO_ECHO):
    # This function takes x measurements and
    # returns the average.
    distance = []
    for y in range(0, x):
        distance.append(simple_measure(GPIO_TRIGGER, GPIO_ECHO))
        time.sleep(0.1)
    for y in range(0, len(distance)):
        distance = distance[y]
    distance = distance / len(distance)
    return distance


def printMeasure(GPIO_TRIGGER, GPIO_ECHO):
    print("Ultrasonic Measurement")
    print("Speed of sound is %s m/s at %s deg" % (speedSound / 100, temperature))

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    # Allow module to settle
    time.sleep(0.5)

    try:
        distance = measure_average_of_3(GPIO_TRIGGER, GPIO_ECHO)
        print("Distance : {0:5.1f}".format(distance))
        time.sleep(0.0001)

    except KeyboardInterrupt:
        # User pressed CTRL-C
        # Reset GPIO settings
        print("Keyboard interrupt ")

    return math.floor(distance)