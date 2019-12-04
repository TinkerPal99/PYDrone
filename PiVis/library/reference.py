__Weather = ["wetter", "Wetter"]
__News = ["Nachrichten", "nachrichten", "News", "news"]
__list1 = ["1", "2", "5", "7"]
__list2 = ["3", "4", "8", "5", "9"]

__x = 0
__y = 0

# def getList_weather():
#   return __Weather


def getList(collection=list):
    return collection


def searchBy(inputcollection=list, compare_collection=list):
    value = False
    for x in range(0, len(inputcollection)):
        for y in range(0, len(compare_collection)):
            if inputcollection[x] == compare_collection[y]:
                value = True
            else:
                y = y + 1
        y = 0
    return value



