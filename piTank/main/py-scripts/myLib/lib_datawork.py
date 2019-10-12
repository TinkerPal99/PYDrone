#! usr/bin/env/python

dataname = "../test.txt"


def openAndRead(dataname):
    f = open(dataname, "r")
    lines = f.readlines()
    f.close
    return lines

def openAndWrite(dataname, text):
    f = open(dataname, "a+")
    f.write(text + "\n")
    f.close
