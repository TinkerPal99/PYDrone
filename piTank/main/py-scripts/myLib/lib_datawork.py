# coding=utf-8
## @package Libraries
#
# <h4>Documentation for this library <u>datawork</u>.</h4>
#
# <p>
# <h5><i>Zweck</i>:</h5> Interaktion mit .txt-Files <br>
# <h5><i>Inhalt</i>:</h5>
# <table><tr>Methoden:
# <td>openAndRead(string:Dateiname)</td>
# <td>openAndWrite(string:Dateiname, string:text)</td>
# <tr></table>
# <p>
#<br><br>
#
# Grundlage dafür ist: <a href="https://www.python-kurs.eu/dateien.php">python-kurs.eu</a>
#_____________________________________________________________________________________________________________


# ! usr/bin/env/python

##Documentation for a variable
#
# Diese Variable dient als default für eine angesprochene Datei.
dataname = "../test.txt"


def openAndRead(dataname):
    ##
    # Documentation for method.
    #
    # openAndRead(string:dateiname)
    #
    # öffnet Datei und liest ihren Inhalt ein. Dieser wird im return-Wert *lines* zurückgegeben.
    f = open(dataname, "r")
    lines = f.readlines()
    f.close
    return lines


def openAndWrite(dataname, text):
    ##
    # Documentation for method.
    #
    # openAndWrite(string:dateiname, string:text)
    #
    # öffnet Datei und liest ihren Inhalt ein. Dieser wird im return-Wert lines zurückgegeben."""

    f = open(dataname, "a+")
    f.write(text + "\n")
    f.close
