__Weather = ["wetter", "Wetter"]
__News = ["Nachrichten", "nachrichten", "News", "news"]


# def getList_weather():
#   return __Weather


def getList(collection=list):
    return collection


def searchBy(collection=list):
    for x in range(0, len(collection)):
        value = str(collection[x])
        x = x + 1
    return value
