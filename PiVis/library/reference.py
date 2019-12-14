import csv

# webpages
_Guardian = "https://www.theguardian.com/world/rss"


# --------------------CSVHandlle----------------------------
def CSVtoList(inputCSV=str):
    outputList = list
    with open(inputCSV) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            ()
        outputList = row
        csvfile.close()
        return outputList


def rewrite_csv(fileName, newRow):
    __new_file = open(fileName, "w")
    __new_file.write(newRow)
    __new_file.close()


# ----------------------listhandle-------------------------------
def getList(collection=list):
    return collection


def searchBy(inputcollection=list, compare_collection=list):
    __value = False
    for x in range(0, len(inputcollection)):
        for y in range(0, len(compare_collection)):
            if inputcollection[x] == compare_collection[y]:
                __value = True
            else:
                y = y + 1
        y = 0
    return __value


def inputToProcess(output=str):
    __recent_input = input(output)
    __splitted_list = __recent_input.split(" ")
    return __splitted_list


def followUp_handle(output=str):
    __status = False
    print ("\n \n \n \n")
    __splitted_list = inputToProcess(output)
    if searchBy(__splitted_list, __Consent):
        __status = True
    return __status


# -------------------------------------------------------------------
try:
    __Weather = CSVtoList("library/csv/Weather.csv")  # ["wetter", "Wetter"]
    __News = CSVtoList("library/csv/News.csv")  # ["Nachrichten", "nachrichten", "News", "news"]
    __Consent = CSVtoList(
        "library/csv/Consent.csv")  # ["Yes", "Jo", "Ja", "Yep", "Jep", "yes", "jo", "ja", "yep", "jep"]
    __Dissent = CSVtoList("library/csv/Dissent.csv")  # ["No", "Nope", "Nep", "Noe", "no", "nope", "nep", "noe"]
    __Note = CSVtoList("library/csv/Note.csv")
    __Notelist = CSVtoList("library/csv/Notes.csv")
    __list1 = ["1", "2", "5", "7"]
    __list2 = ["3", "4", "8", "5", "9"]
except KeyboardInterrupt:
    rewrite_csv("csv/Dissent.csv", ",".join(__Dissent))
    rewrite_csv("csv/Weather.csv", ",".join(__Weather))
    rewrite_csv("csv/News.csv", ",".join(__News))
    rewrite_csv("csv/Consent.csv", ",".join(__Consent))
    print ("Properly rewrote the csv's")
