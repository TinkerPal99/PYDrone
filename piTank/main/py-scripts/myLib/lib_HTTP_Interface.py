#! usr/bin/env/python
import httplib
import time


def request():
    valid_request = False
    try:
        conn = httplib.HTTPConnection("www.muster.de")
        conn.request("Get", "/muster/muster")
        r1 = conn.getresponse()
        # print r1.status, r1.timestamp, r1.address
        if r1.status == 200 and r1.timestamp == time.strftime("%d.%m.%Y %H:%M:%S"):
            valid_request = True
            valid_address = r1.adress
        conn.close()
    except:
        print "Server not reachable"

    return valid_request, valid_address


def check_payment():
    got_payment = False
    try:
        conn = httplib.HTTPConnection("paymentadress")
        conn.request("Get", "/dies/dort")
        r1 = conn.getresponse()
        if r1.status == 200 and conn.request("Get", "Bezahlstatus") == True:
            got_payment = True
        conn.close()
    except:
        print "Server not reachable"

    return got_payment
