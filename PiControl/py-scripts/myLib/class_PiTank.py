# coding=utf-8
## @package classes
#
# <h4>Documentation for this class-library <u>class_PiTank.py</u>.</h4>
#
# <p>
# <h5><i>Zweck</i>:</h5> Objektorientierte Klasse zum Arbeiten mit einem Rover (Modell: PiTank) <br>
# <h5><i>Inhalt</i>:</h5>
# <table>
# <tr>PiTank</tr>
#   <tr><b>set</b>
#       <td>__init__(self ,int:pin ,int:pin , int:pwm ,int:pwm ,int:pin ,int:pin, int:pin ,int:pin)</td>
#       <td>set_lamp(self ,int:pin ,int:pin)</td>
#       <td>set_Forward_Sensor(self ,int:pin ,int:pin)</td>
#       <td>set_Backward_Sensor(self ,int:pin ,int:pin)</td>
#   </tr>
#   <tr><b>get</b>
#       <td>print_Sensor(self)</td>
#       <td>print_motor_h(self)</td>
#   </tr>
#   <tr><b>Actions</b>
#       <td>vehicle_drive(self ,string:Richtung)</td>
#       <td>start_pwm(self, int:Startpuls)</td>
#       <td>change_pwm(self, int:neuer Puls rechts, int:neuer Puls links)</td>
#       <td>stop_pwm(self)</td>
#    </tr>
# </table>
# <p>
# <br><br>
#
#
# _____________________________________________________________________________________________________________


# ! usr/bin/env/python
import lib_movement
import RPi.GPIO as GPIO


class PiTank:

    def __init__(self, enableA, enableB, maximum_pulse, port1, port2, port3, port4):
        ##
        # Documentation of initialize for class PiTank.
        #
        # <b>__init__(self ,int:pin ,int:pin , int:pwm ,int:pwm ,int:pin ,int:pin, int:pin ,int:pin)</b>
        #
        # Setzt die enables des Motortreibers, den Maximum an Puls in Millihertz sowie die grundlegenen Pins für den
        # Betrieb der Motoren.<br><br>
        self.wheelleft_pwm = GPIO.PWM(enableB, maximum_pulse)
        ##
        # Documentation for variable <b>wheelleft_pwm</b>
        #
        # Dient der Pulsweitenmodulation für die linke Seite.
        self.wheelright_pwm = GPIO.PWM(enableA, maximum_pulse)
        ##
        # Documentation for variable <b>wheelright_pwm</b>
        #
        # Dient der Pulsweitenmodulation für die rechte Seite.
        self.enableA = enableA
        ##
        # Documentation for variable <b>enableA</b>
        #
        # Festlegung des enableA-Pins.
        self.enableB = enableB
        ##
        # Documentation for variable <b>enableB</b>
        #
        # Festlegung des enableB-Pins.
        self.port1 = port1
        ##
        # Documentation for variable <b>port1</b>
        #
        # Festlegung des Port1-Pins für die H-Brücke.
        self.port2 = port2
        ##
        # Documentation for variable <b>port2</b>
        #
        # Festlegung des Port2-Pins für H-Brücke.
        self.port3 = port3
        ##
        # Documentation for variable <b>port3</b>
        #
        # Festlegung des Port3-Pins für H-Brücke.
        self.port4 = port4
        ##
        # Documentation for variable <b>port4</b>
        #
        # Festlegung des Port4-Pins für H-Brücke.

    def set_lamp(self, lampA, lampB):
        ##
        # Documentation of setter for class PiTank.
        #
        # <b>set_lamp(self ,int:pin ,int:pin)</b>
        #
        # Setzt die Kontrolllampen für den Motorbetrieb.
        self.lampA = lampA
        ##
        # Documentation for variable <b>lampA</b>
        #
        # Festlegung des lampA-Pin für Motorkontrolle.
        self.lampB = lampB
        ##
        # Documentation for variable <b>lampB</b>
        #
        # Festlegung des lampB-Pin für Motorkontrolle.

    def set_Forward_Sensor(self, GPIO_TRIGGER, GPIO_ECHO):
        ##
        # Documentation of setter for PiTank.vorderer Sensor
        #
        # <b>set_Forward_Sensor(self ,int:pin ,int:pin)</b>
        #
        # Setzt die Pins für den Betrieb eines vorderen Schallabstandsensors, 4-Pin.
        self.GPIO_TRIGGER_FORWARD = GPIO_TRIGGER
        self.GPIO_ECHO_FORWARD = GPIO_ECHO

    def set_Backward_Sensor(self, GPIO_TRIGGER, GPIO_ECHO):
        ##
        # Documentation of setter for PiTank.hinterer Sensor
        #
        # <b>set_Backward_Sensor(self ,int:pin ,int:pin)</b>
        #
        # Setzt die Pins für den Betrieb eines hinteren Schallabstandsensors, 4-Pin.
        self.GPIO_TRIGGER_BACKWARD = GPIO_TRIGGER
        self.GPIO_ECHO_BACKWARD = GPIO_ECHO

    def print_Sensor(self):
        ##
        # Documentation of getter for PiTank.Sensor
        #
        # <b>print_Sensor(self)</b>
        #
        # Gibt die aktuelle, eingestellte Pinbelegung für beide Sensoren aus.
        print("GPIO_TRIGGER_FORWARD" + str(self.GPIO_TRIGGER_FORWARD))
        print("GPIO_ECHO_FORWARD" + str(self.GPIO_ECHO_FORWARD))
        print("GPIO_TRIGGER_BACKWARD" + str(self.GPIO_TRIGGER_BACKWARD))
        print("GPIO_ECHO_BACKWARD" + str(self.GPIO_ECHO_BACKWARD))

    def print_motor_h(self):
        ##
        # Documentation of getter for PiTank.Motortreiber H-Brücke
        #
        # <b>print_motor_h(self)</b>
        #
        # Gibt die aktuelle, eingestellte Pinbelegung für den Motorenbetrieb aus.
        print("enableA" + str(self.enableA))
        print("enableB" + str(self.enableB))
        print("port1" + str(self.port1))
        print("port2" + str(self.port2))
        print("port3" + str(self.port3))
        print("port4" + str(self.port4))
        print("lampA" + str(self.lampA))
        print("lampB" + str(self.lampB))

    def vehicle_drive(self, direction):
        ##
        # Documentation of action for PiTank.vehicle_drive
        #
        # <b>vehicle_drive(self ,string:Richtung)</b>
        #
        # Lässt den Wagen in die genannte Richtung fahren.
        # Optionen: (String) forward, backward, stop, leftturn, rightturn
        # Falsche Eingaben werden nicht bearbeitet.
        if direction == "forward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_FORWARD(self.lampA, self.port3, self.port4)
        elif direction == "backward":
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
            lib_movement.wheel_left_BACKWARD(self.lampA, self.port3, self.port4)
        elif direction == "stop":
            lib_movement.clean(self.lampA, self.port1, self.port2, self.lampB, self.port3, self.port4)
            # print ("Stopped")
        elif direction == "leftturn":
            lib_movement.wheel_left_BACKWARD(self.lampA, self.port3, self.port4)
            lib_movement.wheel_right_FORWARD(self.lampB, self.port1, self.port2)
        elif direction == "rightturn":
            lib_movement.wheel_left_FORWARD(self.lampA, self.port3, self.port4)
            lib_movement.wheel_right_BACKWARD(self.lampB, self.port1, self.port2)
        else:
            print ("Wrong input")

    def start_pwm(self, startpulse):
        ##
        # Documentation of action for PiTank.start pwm
        #
        # <b>start_pwm(self, int:Startpuls)</b>
        #
        # Setzt Enabler für den Motor auf true und startet Pulsweitenmodulation zur Geschwindigkeitskontrolle.<br>
        # Der Puls wird als Integer angegegben, umso höher der Wert umso schneller der Wagen. Meine Empfehlung
        # ist 100.
        self.wheelright_pwm.start(startpulse)
        self.wheelleft_pwm.start(startpulse)

    def change_pwm(self, changepulse_right, changepulse_left):
        ##
        # Documentation of action for PiTank.wechsel pwm
        #
        # <b>change_pwm(self, int:neuer Puls rechts, int:neuer Puls links)</b>
        #
        # Enabler bleiben aktiviert und ändern den Puls zur Variierung der Geschwindigkeit<br>
        # Der Puls wird als Integer angegegben, umso höher der Wert umso schneller der Wagen. Meine Empfehlung
        # ist ein Wert kleiner dem Startwert.
        self.wheelleft_pwm.ChangeDutyCycle(changepulse_left)
        self.wheelright_pwm.ChangeDutyCycle(changepulse_right)

    def stop_pwm(self):
        ##
        # Documentation of action for PiTank.stopp pwm
        #
        # <b>stop_pwm(self)</b>
        #
        # Enabler werden deaktiviert. Der Wagen hält an.<br>
        self.wheelleft_pwm.stop()
        self.wheelright_pwm.stop()
