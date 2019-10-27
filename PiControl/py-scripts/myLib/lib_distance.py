# coding=utf-8
## @package Libraries
#
# <h4>Documentation for this library <u>lib_distance.py</u>.</h4>
#
# <p>
# <h5><i>Zweck</i>:</h5> Methoden zur Anbindung eines schallbasierten 4-Pin Abstandssensor <br>
# <h5><i>Inhalt</i>:</h5>
# <table><tr>Methoden:
# <td>simple_measure(int:pin ,int:pin)</td>
# <td>measure_average_of_3(int:pin ,int:pin)</td>
# <td>measure_average_of_x(int:Anzahl der Wiederholungen, int:pin, int:pin)</td>
# <td>printSettings(_)</td>
# <td>print_formattedMeasure(int:pin, int:pin)</td>
# <tr></table>
# <p>
# _____________________________________________________________________________________________________________

# ! usr/bin/env/python
import math
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

##Documentation for a variable "temperature"
#
# Diese Variable dient als Temperaturwert für die Schallgeschwindigkeitsberechnung.
temperature = 20

##Documentation for a variable "speedSound"
#
# Schallgeschwindigkeit in cm/s auf Temperatur
speedSound = 33100 + (0.6 * temperature)


def simple_measure(GPIO_TRIGGER, GPIO_ECHO):
    ##
    # Documentation for method
    # <b>simple_measure(int:pin ,int:pin)</b>
    #Vollführt eine einfache Messung über einen Schallabstandssensorr auf angegebenen Pins.
    #Dabei wird eine Signal vom Trigger ausgestoßen, einen kurzen Moment gewartet unf dann der Zeitabstand bis zum reflektierten Eingang des Signals abgewartet.
    #Aus diesem Wert wird dann der Abstand in cm berechnet.
    #*Formel*: Abstand = (Zeitunterschied * Schallgeschwindigkeit)/2
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    start = time.time()

    while True:
        if GPIO.input(GPIO_ECHO) == 0:
            start = time.time()
            time.sleep(0.01)
        if GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()
            elapsed = stop - start
            distance = (elapsed * speedSound) / 2
            break
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

    # init distance_list as a list
    # set distance as 0
    distance_list = []
    distance = 0
    # take x measurements und append them to the list
    for y in range(0, x):
        distance_list.append(simple_measure(GPIO_TRIGGER, GPIO_ECHO))
        time.sleep(0.1)
    for y in range(0, len(distance_list)):
        # now sum all entries of the list up
        distance = distance + distance_list[y]
        # take average by dividing summed distance with lenght of the list
        distance_q = distance / len(distance_list)
    return distance_q


def printSettings():
    print("Ultrasonic Measurement")
    print("Speed of sound is %s m/s at %s deg" % (speedSound / 100, temperature))


def print_formattedMeasure(GPIO_TRIGGER, GPIO_ECHO):
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
        GPIO.cleanup()
    return math.floor(distance)
