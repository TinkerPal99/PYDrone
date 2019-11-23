# coding=utf-8
# !usr/bin/env/python
import datetime

import RPi.GPIO as GPIO
from myLib import lib_gy521, class_PiControl
import time, urllib2, logging, sys, os

GPIO.setmode(GPIO.BOARD)
#----------------------------logging_basicconfig---------------------
logging.basicConfig(
    filename = "logs/init.log",
    filemode ="a")
#Ausgabe auf terminal
__log_handler = logging.StreamHandler(sys.stdout)

#setzen eines eigenen Loggerfromats
__log_form = logging.Formatter("%(asctime)s %(levename)s: %(messages)s", "%d.%m.%Y %H:%M:%S")
__log_handler.setFormatter(__log_form)
__logger = logging.getLogger()
__logger.addHandler(__log_handler)
#Standardloglevel einsetzen
__logger.setLevel(logging.DEBUG)

currentDir = os.getcwd()
#TODO Remove unused datetime
#dateTimeObj = datetime.now()
#datestamp = dateTimeObj.strftime("%Y-%m-%d")
# --------------------------Preparation---------------------------------------------------------------------------------
callIP = "http://192.168.8.200/main/"
saveSpace = "/savings"
LAMP_Y = 1
LAMP_G = 1

piControl = class_PiControl.PiControl(callIP, saveSpace)
logging.log(logging.INFO,"CallIP set as " + callIP +". Storage for savings set as " + currentDir + saveSpace)


Taster = 20
GPIO.setup(LAMP_Y, GPIO.IN)
GPIO.setup(LAMP_G, GPIO.IN)

# -----------------------------MAIN-------------------------------------------------------------------------------------
while True:
    try:
        if GPIO.input(Taster) == GPIO.HIGH:
            while True:
                piControl.gyro_CallOnRead(piControl.gyro_read())
                time.sleep(0.5)
                if GPIO.input(Taster) == GPIO.HIGH:
                    GPIO.output(LAMP_Y) = GPIO.HIGH
                    GPIO.output(LAMP_G) = GPIO.LOW
                    time.sleep(5)
                    break
        time.sleep(0.01)
    except urllib2.URLError:
        logging.log(logging.DEBUG,"Fehler - urllib")
    except KeyboardInterrupt:
        logging.log(logging.INFO,"Abbruch - keybord interrupt")
        logging.shutdown()
    except Exception as unknown:
        logging.log(logging.CRITICAL,"Abbruch - Kritischer unbekannter Fehler")
        logging.shutdown()
