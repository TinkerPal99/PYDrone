#! usr/bin/env/python
import lib_gy521
import RPi.GPIO as GPIO
import urllib, time


class PiControl:
    def __init__(self, address):
        self.gyro_out = []
        self.destination_address = address

    def get_call_address(self):
        print(self.destination_address)

    def call_address(self, address_appendix):
        urllib.urlopen(self.destination_adress + address_appendix)

    def gyro_read(self):

        gyroskop_xout = lib_gy521.read_word_2c(0x43)
        gyroskop_yout = lib_gy521.read_word_2c(0x45)
        gyroskop_zout = lib_gy521.read_word_2c(0x47)

        # print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 100))
        # print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 100))
        # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 100))

        gy_x_skal = gyroskop_xout / 100
        gy_y_skal = gyroskop_yout / 100
        gy_z_skal = gyroskop_zout / 100
        time.sleep(1)

        self.gyro_out.append(gy_x_skal)
        self.gyro_out.append(gy_y_skal)
        self.gyro_out.append(gy_z_skal)

        # print (gy_x_skal)
        # print (gy_y_skal)
        # print (gy_z_skal)

        return self.gyro_out

    def gyro_CallOnRead(self, gyro_out):
        if self.gyro_out[1] >= 40:
            print("forward")
            self.call_address("RPS1.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS1.php")
        elif self.gyro_out[1] <= -40:
            print("backward")
            self.call_address("RPS5.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS5.php")
        elif self.gyro_out[0] >= 50:
            print("right")
            self.call_address("RPS5.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS4.php")
        elif self.gyro_out[0] <= -50:
            print("left")
            self.call_address("RPS3.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS3.php")
        elif self.gyro_out[2] >= 50:
            print("down")
            self.call_address("RPS2.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS2.php")
        elif self.gyro_out[2] <= -50:
            print("up")
            self.call_address("RPS2.php")
            # urllib.urlopen("http://192.168.8.200/main/RPS2.php")
