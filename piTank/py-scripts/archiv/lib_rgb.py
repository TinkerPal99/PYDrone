# coding=utf-8
## @package archive
# <h4>Documentation for this library <u>"rgb"</u>.</h4>
#
# <p>
# <h5><i>Zweck</i>:</h5> Betreiben verschiedener zweipoliger Signallampen <br>
# <h5><i>Inhalt</i>:</h5>
# !WIP!
# <table><tr>Methoden:
# <td>clean(int:pin ,int:pin, int:pin)</td>
# <td>light(int:pin ,int:pin, int:pin)</td>
# <td>blink_left(int:pin ,int:pin, int:pin)</td>
# <td>bl(int:pin ,int:pin, int:pin)</td>
# <td>br(int:pi, int:pi)</td>
# <tr></table>
# <p>
#<br><br>
#

#_____________________________________________________________________________________________________________


#! usr/bin/env/python
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#backward
GPIO.setup(40, GPIO.OUT)
#forward
GPIO.setup(38, GPIO.OUT)
#blink-right
GPIO.setup(33, GPIO.OUT)
#blink-left
GPIO.setup(31, GPIO.OUT)

def clean():
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
   # GPIO.output(36, GPIO.LOW)
   # GPIO.output(26, GPIO.LOW)
    return

def light():
   GPIO.output(40, GPIO.LOW)
   GPIO.output(38, GPIO.LOW)
  # GPIO.output(29, GPIO.HIGH)
  # GPIO.output(26, GPIO.HIGH)
   return
def blink_left():
    GPIO.output(31, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(31, GPIO.HIGH)
    time.sleep(1)
    return
def blink_right():
    GPIO.output(33, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(33, GPIO.HIGH)
    time.sleep(1)
    return


def  bl(y):
    a = 0
    while a < y:
        blink_left()
        a = a + 1
    return

def  br(y):
    b = 0
    while b < y:
        blink_right()
        b = b + 1
    return


while 1:
#Datei oeffnen zum lesen, dies jedesmal zu Beginn der Schleife um auf Veraenderungen zu reagieren
	f = open("../test.txt", "r")
	lines = f.readlines()
	f.close
	print lines
	time.sleep(0.5);
#Datei oeffnen zum bearbeiten
	for line in lines:
		f = open("../test.txt", "w")
		if "LLL1" in line:
			print "Enabled LLL1";
			GPIO.output(38, GPIO.HIGH)
			GPIO.output(40, GPIO.HIGH)
			GPIO.output(31, GPIO.HIGH)
			GPIO.output(33, GPIO.HIGH)
			print "Disabled LLL1"
       		elif "LLL2" in line:
			print "Enabled blink left";
			bl(20)
			time.sleep(1)
			clean()
			print "Disabled LLL2"
		elif "LLL3" in line:
			print "Enabled blink right";
			br(20)
			time.sleep(1)
			clean()
		elif "LLL4" in line:
			print "Enabled bright Light"
			light()
       		elif "LLL_clean" in line:
               		print "Cleaned"
			clean()
       		elif "RHF" in line:
			()
		elif "RPS" in line:
			()
		elif " " in line:
			time.sleep(3)
			print "Waiting for Query"
			time.sleep(3)
		else:
			f.write(line)
			print "Disabled"
			clean();
			time.sleep(0.5)
	f.close


