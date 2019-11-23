#! usr/bin/env/python
import lib_gy521
import RPi.GPIO as GPIO
import urllib2, time, datetime

class PiControl:
    def __init__(self, address, path):
        self.__gyro_out = []
        self.destination_address = address
        self.__cam = PiCamera()
        self.path_for_savings = path
#----------------------------cam----------------------------------------------------------------
    def setSettings_of_Cam(width, height, framerate):
        self.cam.resolution = (width, height)
        self.cam.framerate = framerate


    def printSettings_of_Cam(self):
        print ("Resolution " + self.cam.resolution)
        print ("Framerate" + self.cam.framerate)


    def Cam_preview(self, lenght):
        camera.start_preview()
        time.sleep(lenght)
        camera.stop_preview()


    def Cam_takePic(self):
        name = self.path_for_savings + "/" + datetime.now()
        try:
            camera.capture(name)
            summary = ("Shot is taken and saved as " + name  )
        except PiCameraError:
            summary = ("Something with the camera went wrong")
        except ValueError or PiCameraError :
            summary = ("Please check your path.")
        return summary


    def Cam_takeCaptionedPic(self, text):
        name = self.path_for_savings + "/" + datetime.now()
        camera.annotate_text = text
        try:
            camera_takePic(name)
            summary = ("Shot is taken and saved as " + name)
            camera.annotate_text = ""
        except PiCameraError:
            summary = ("Something with the camera went wrong")
        except ValueError or PiCameraError:
            summary = ("Please check your path.")
        return summary


    def Cam_takeShot(self, length):
        name = self.path_for_savings + "/" + datetime.now()
        try:
            camera.start_recording(name)
            time.sleep(length)
            camera.stop_recording()
            summary = ("Shot is taken and saved as " + name  )
        except PiCameraError:
            summary = ("Something with the camera went wrong")
        except ValueError or PiCameraError :
            summary = ("Please check your path.")
        return summary

#-----------------------------------webacess------------------------------------
    def get_call_address(self):
        print(self.destination_address)

    def call_address(self, address_appendix):
        urllib.urlopen(self.destination_adress + address_appendix)
#------------------------------gyro---------------------------------------------
    def gyro_read(self):

        __gyroskop_xout = lib_gy521.read_word_2c(0x43)
        __gyroskop_yout = lib_gy521.read_word_2c(0x45)
        __gyroskop_zout = lib_gy521.read_word_2c(0x47)

        # print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 100))
        # print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 100))
        # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 100))

        __gy_x_skal = gyroskop_xout / 100
        __gy_y_skal = gyroskop_yout / 100
        __gy_z_skal = gyroskop_zout / 100
        time.sleep(1)

        self.__gyro_out.append(gy_x_skal)
        self.__gyro_out.append(gy_y_skal)
        self.__gyro_out.append(gy_z_skal)

        # print (gy_x_skal)
        # print (gy_y_skal)
        # print (gy_z_skal)

        return self.__gyro_out

    def gyro_CallOnRead(self, gyro_out):
        if self.__gyro_out[1] >= 40:
            print("forward")
            self.call_address("RPS1.php")
            urllib.urlopen("http://192.168.8.200/main/RPS1.php")
        elif self.__gyro_out[1] <= -40:
            print("backward")
            self.call_address("RPS5.php")
            urllib.urlopen("http://192.168.8.200/main/RPS5.php")
        elif self.__gyro_out[0] >= 50:
            print("right")
            self.call_address("RPS5.php")
            urllib.urlopen("http://192.168.8.200/main/RPS4.php")
        elif self.__gyro_out[0] <= -50:
            print("left")
            self.call_address("RPS3.php")
            urllib.urlopen("http://192.168.8.200/main/RPS3.php")
        elif self.__gyro_out[2] >= 50:
            print("down")
            self.call_address("RPS2.php")
            urllib.urlopen("http://192.168.8.200/main/RPS2.php")
        elif self.__gyro_out[2] <= -50:
            print("up")
            self.call_address("RPS2.php")
            urllib.urlopen("http://192.168.8.200/main/RPS2.php")
