# coding=utf-8
## @package tryouts
# <h4>Documentation for this tryout <u>license.py</u>.</h4>
# <br>
#<p>
# <h5><i>Zweck</i>:</h5> Aktivierung einzelner Dienste durch das Auslesen von "Zertifikaten" <br>
# <h5><i>Inhalt</i>:</h5>
# <table><tr>Methoden:
# <td>noch kein geordneter Inhalt</td>
# <td></td>
# <tr></table>
# <p>
#<br><br>
#
#
#_____________________________________________________________________________________________________________

#! usr/bin/env/python
import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

counter = 0
##
# Documentation for variable <b>counter</b>
#
# Dient einer verringerten Ausgabe über Prompt
license_path = "../Lizenzen/"
##
# Documentation for variable <b>license_path</b>
#
# Defaultpfad für Pfad zum auslesen der Lizenz

while 1:
    print os.listdir(license_path)
    time.sleep(0.5)

    while "Modul1.txt" in os.listdir(license_path):
        print "Modul 1, aktiv"
        time.sleep(120)

    while "Modul2.txt" in os.listdir(license_path):
        print "Modul 2, aktiv"
        time.sleep(120)
#Scheint dÃ¤mlich, oder ? Der folgende Abschnitt druckt einen Bescheid, dass keine aktive Lizenz besteht. Damit die Prompt aber nicht zugespammt wird, tut er dies nur alle 240000 Sekunden
    counter = counter + 1

    if counter == 200:
        print "No active License"
        counter = 0
