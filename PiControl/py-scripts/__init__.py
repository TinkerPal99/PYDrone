# coding=utf-8
#! usr/bin/env/python

import RPi.GPIO as GPIO
from myLib import lib_gy521
import urllib
import time
import os

GPIO.setmode(GPIO.BOARD)
gyro = [0, 0]

a = "../Lizenzen/"


def gyroskope():
    gyroskop_xout = lib_gy521.read_word_2c(0x43)
    gyroskop_yout = lib_gy521.read_word_2c(0x45)
    # gyroskop_zout = lib_gy521.read_word_2c(0x47)

#TODO Entfernen des folgenden Blocks 19.11.2019
    # print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
    # print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
    # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))

    gy_x_skal = (gyroskop_xout / 100) - 40
    gy_y_skal = gyroskop_yout / 100
    # gy_z_skal = gyroskop_zout / 100
    time.sleep(1)

    gyro[0] = gyro[0] + gy_x_skal
    gyro[1] = gyro[1] + gy_y_skal

    print ("[" + str(gyro[0]) + "][" + str(gyro[1]) + "]")
    return gyro


while True:
    try:
        while "Modul1.txt" in os.listdir(a):

            gyro = gyroskope()

            if gyro[0] <= -30:
                print("forward")
                urllib.urlopen("http://192.168.8.200/main/RPS1.php")
                time.sleep(0.1)
            elif gyro[0] >= 30:
                print("stop!")
                urllib.urlopen("http://192.168.8.200/main/RPS2.php")
                time.sleep(0.1)
            elif gyro[1] >= 40:
                print("right")
                urllib.urlopen("http://192.168.8.200/main/RPS4.php")
                time.sleep(1)
            elif gyro[1] <= -40:
                print("left")
                urllib.urlopen("http://192.168.8.200/main/RPS3.php")
                time.sleep(1
                           )
    except KeyboardInterrupt:
        print ("Manual break")
        break
