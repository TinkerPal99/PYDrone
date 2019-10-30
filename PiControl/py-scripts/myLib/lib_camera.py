#!usr/bin/env/python

from picamera import PiCamera
import time

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15


def camera_preview():
    camera.start_preview()
    time.sleep(1)
    camera.stop_preview()


def camera_takePic(path):
    camera.capture(path)


def camera_takeShot(path, length):
    camera.start_recording(path)
    time.sleep(length)
    camera.stop_recording()


def camera_takePic_with(text, path):
    camera.annotate_text = text
    camera_takePic(path)
