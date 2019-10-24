# coding=utf-8
## @package testset
# <h4>Documentation for this testset <u>Motortest.py</u>.</h4>
# <br>
#<p>
# <h5><i>Zweck</i>:</h5> Abprüfen einzelner Fahrfunktionen <br>
# <h5><i>Inhalt</i>:</h5>
# <table><tr>testcases:
# <td>main(int:Fahranweisung)</td>
# <td>printPin(_)</td>
# <tr></table>
# <p>
#<br><br>
#
#
#_____________________________________________________________________________________________________________

#! usr/bin/env/python
import time
import RPi.GPIO as GPIO
import lib_movement

enableA = 36
port1 = 40
port2 = 38
port3 = 35
port4 = 37
enableB = 32

GPIO.setup(enableA, GPIO.OUT)  # EnA
GPIO.setup(enableB, GPIO.OUT)  # EnB

GPIO.setup(36, GPIO.OUT)  # EnA
GPIO.setup(32, GPIO.OUT)  # EnB

GPIO.setup(port1, GPIO.OUT)  # 1
GPIO.setup(port2, GPIO.OUT)  # 2
GPIO.setup(port3, GPIO.OUT)  # 3
GPIO.setup(port4, GPIO.OUT)  # 4

# Defining pwm
motor1GPIO = GPIO.PWM(enableA, 100)
motor2GPIO = GPIO.PWM(enableB, 100)

dc = 70  # set speed max - 100; min - 35

motor1GPIO.start(dc)
motor2GPIO.start(dc)


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_usecases_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_
def main(x):
    ##
    # Documentation for this testcase.<br>
    #
    # <b>main(int:Fahranweisung)</b><br>
    #
    # Lässt das vordefinierten Räder drehen. Der Parameter bestimmt die Geschwindigkeit 0 = Schnell, 1 = Langsam.

    #x = input("Modus: Schnell Fahren(0) Langsam Fahren(1): ")

    if x == 0:
        print ("Start rechts rueckwaerts")
        lib_movement.wheel_right_BACKWARD(port1, port2)
        print ("Start links rueckwaerts")
        lib_movement.wheel_left_BACKWARD(port3, port4)
        time.sleep(10)
        print ("Change duty cycle")
        motor1GPIO.ChangeDutyCycle(35)
        motor2GPIO.ChangeDutyCycle(35)
        time.sleep(5)
        lib_movement.clean(enableA, enableB, port1, port2, port3, port4)


def printPin():
    ##
    # Documentation for this testcase.<br>
    #
    # <b>printPin(_)</b><br>
    #
    # Lässt das vordefinierten Pins einmal auf die Ausgabe geben.
    print ("enable A: " + str(enableA))
    print ("port 1: " + str(port1))
    print ("port 2: " + str(port2))
    print ("____________________")
    print ("enable B: " + str(enableB))
    print ("port 3: " + str(port3))
    print ("port 4: " + str(port4))


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_testplan_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
main()
# printPin()
motor1GPIO.stop()
motor2GPIO.stop()

time.sleep(1)
print ("Done...")
