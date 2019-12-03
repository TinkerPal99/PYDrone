# https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
import feedparser

# __ExampleFeed = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
__ExampleFeed = "http://www.tagesschau.de/xml/rss2"


def checkNewFeed(feed=str):
    NewsFeed = feedparser.parse(__ExampleFeed)
    entry = NewsFeed.entries[1]
    print entry.keys()


def loadFeed(feed=str):
    __newsFeed = feedparser.parse(feed)
    return __newsFeed


def show_5_Entries_of(feed=str):
    __feed = loadFeed(feed)
    if len(__feed) < 4:
        for x in range(0, len(__feed)):
            x = x + 1
            entry = __feed.entries[x]
            print ("Post Title : -" + entry.title + "- from " + entry.link)
            print ("###########################")
            print (entry.summary)
            print ("___________________________________________________________________________________________")
    else:
        for x in range(0, 4):
            x = x + 1
            entry = __feed.entries[x]
            print ("Post Title : -" + entry.title + "- from " + entry.link)
            print ("###########################")
            print (entry.summary)
            print ("___________________________________________________________________________________________")


show_5_Entries_of("http://www.tagesschau.de/xml/rss2")
# checkNewFeed("http://www.tagesschau.de/xml/rss2")