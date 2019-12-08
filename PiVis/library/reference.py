__Weather = ["wetter", "Wetter"]
__News = ["Nachrichten", "nachrichten", "News", "news"]
__Consent = ["Yes", "Jo", "Ja", "Yep", "Jep", "yes", "jo", "ja", "yep", "jep"]
__Dissent = ["No", "Nope", "Nep", "Noe", "no", "nope", "nep", "noe"]
__list1 = ["1", "2", "5", "7"]
__list2 = ["3", "4", "8", "5", "9"]

# webpages
_Guardian = "https://www.theguardian.com/world/rss"

__x = 0
__y = 0


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
