# coding=utf-8
## @package Libraries
#
# <h4>Documentation for this library <u>lib_HTTP_Interface.py</u>.</h4>
#
# <p>
# <h5><i>Zweck</i>:</h5> Restaufrufe <br>
# <h5><i>Inhalt</i>:</h5>
# <table><tr>Methoden:
# <td>request(_)</td>
# <td>ckeck_payment(non_functional)</td>
# <tr></table>
# <p>
# <br><br>
#
#
# _____________________________________________________________________________________________________________

# ! usr/bin/env/python
from __future__ import print_function
import httplib
import time


def request(adresse, path):
    ##
    # Documentation for method.
    #
    # <b>request(_)</b>
    # !WIP!
    # schickt Anfrage an Adresse
    try:
        conn = httplib.HTTPConnection(adresse)
        conn.request("Get", path)
        r1 = conn.getresponse()
        answer = True

    except:
        print ("Server not reachable")
        answer = False
    return answer


def check_payment():
    ##
    # Documentation for method.
    # !WIP!
    # <b>check_payment(_)</b>
    # !WIP!
    # schickt Anfrage an Adresse, überprüft einen Wert und gibt boolean als return-Wert
    got_payment = False
    try:
        conn = httplib.HTTPConnection("paymentadress")
        conn.request("Get", "/dies/dort")
        r1 = conn.getresponse()
        if r1.status == 200 and conn.request("Get", "Bezahlstatus") == True:
            got_payment = True
        conn.close()
    except:
        print("Server not reachable")

    return got_payment
