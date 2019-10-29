# coding=utf-8
#! usr/bin/env/python

import RPi.GPIO as GPIO
from myLib import lib_gy521
import urllib
import time


while True:
    gyroskop_xout = lib_gy521.read_word_2c(0x43)
    gyroskop_yout = lib_gy521.read_word_2c(0x45)
    gyroskop_zout = lib_gy521.read_word_2c(0x47)

    # print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
    # print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
    # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))

    gy_x_skal = gyroskop_xout / 100
    gy_y_skal = gyroskop_yout / 100
    gy_z_skal = gyroskop_zout / 100
    time.sleep(1)

    # print (gy_x_skal)
    # print (gy_y_skal)
    # print (gy_z_skal)

    if gy_x_skal >= 40:
        print("forward")
        urllib.urlopen("http://192.168.8.200/main/RPS1.php")
    elif gy_x_skal <= -40:
        print("backward")
        urllib.urlopen("http://192.168.8.200/main/RPS5.php")
    elif gy_y_skal >= 50:
        print("right")
        urllib.urlopen("http://192.168.8.200/main/RPS4.php")
    elif gy_y_skal <= -50:
        print("left")
        urllib.urlopen("http://192.168.8.200/main/RPS3.php")
    elif gy_z_skal >= 50:
        print("down")
        urllib.urlopen("http://192.168.8.200/main/RPS2.php")
    elif gy_z_skal <= -50:
        print("up")
        urllib.urlopen("http://192.168.8.200/main/RPS2.php")

