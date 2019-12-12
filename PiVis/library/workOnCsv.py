import csv

__Build = 60
__VinVorrat = 100
__Path_Vins = "C:/Users/eising/PycharmProjects/Automatisierung/venv/Imports/Vins.csv"
__Path_Csv = "C:/Users/eising/PycharmProjects/Automatisierung/venv/Imports/BAUNEE4MZ19030104/BAUNEE4MZ19030104.csv"


# __Path_csv = "/var/apphome/890_autest/890_autest-0/.jenkins/workspace/Sulzer/Playground_M/OUD-C-P/OUDCore_SPIN_And_VeConf/src/test/java/python/Automatisierung/venv/Imports/BAUNEE4MZ19030104/BAUNEE4MZ19030104.csv"
# __Path_Vins = "/var/apphome/890_autest/890_autest-0/.jenkins/workspace/Sulzer/Playground_M/OUD-C-P/OUDCore_SPIN_And_VeConf/src/test/java/python/Automatisierung/venv/Imports/Vins.csv"
# build = int(input("Input Build hier: "))


def rewrite_csv(fileName, newRow):
    __new_file = open(fileName, "w")
    __new_file.write(newRow)
    __new_file.close()


try:
    # Modul sys wird importiert:
    import sys

    with open(__Path_Vins) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print ("Alte Vin-CSV ist: " + str(row))
            vins = row

    with open(__Path_Csv) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print ("Alte CTAT-CSV ist: " + str(row))

    liste = []
    for eachArg in sys.argv:
        print (eachArg)
        liste.append(eachArg)

    index = int(liste[1]) - __Build
    print ("Zugriff auf die " + str(index) + ". Vin in der Liste.")
    row[4] = vins[index]
    string = ",".join(row)
    rewrite_csv(__Path_Csv, string)
    print ("Achtung! Es sind nurnoch " + str(__VinVorrat - index) + ". Vins in ihrer Liste unverbraucht.")

 except TypeError:
    print ("TypeError! Please control types of imported data.")
    exit(1)
except ReferenceError:
    print ("ReferenceError! File not found.")
    exit(2)
except IndexError:
    print ("CSV is to short, please take a look at them.")
    exit(3)
except SyntaxError:
    print ("Please look at your python-version. Use the python -version command at shell. This Code runs on 2.7")
    exit(4)
except ImportError:
    print ("Module not found. This code needs the csv-module of python 2.7.11.")
    exit(5)
except RuntimeError:
    print ("Complex Error (RuntimeError). Please take a look at the code.")
    exit(6)
except OSError:
    print ("Complex Error (OSError). Please take a look at the enviroment and OS.")
    exit(7)
except MemoryError:
    print (
        "Complex Error (MemoryError). Please give this application more memory to work with or shorten the input data.")
    exit(8)
