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


def print_splittedEntry_of(summary, sign=str):
    __splitted_entry = summary.split(sign)
    __splitted_entry.pop()
    for x in range(0, len(__splitted_entry)):
        print __splitted_entry[x]
        x = x + 1


def feedEntry(feed, entry):

    entry = feed.entries[entry]
    print ("Post Title : -" + entry.title + "- from " + entry.link)
    print ("############################################################################################")
    print_splittedEntry_of(entry.summary, "</p>")
    print ("___________________________________________________________________________________________")


def show_5_Entries_of(feed=str):
    __feed = loadFeed(feed)
    if len(__feed) < 4:
        for x in range(0, len(__feed)):
            x = x + 1
            feedEntry(__feed, x)
    else:
        for x in range(0, 4):
            x = x + 1
            feedEntry(__feed, x)


# show_5_Entries_of("https://www.theguardian.com/world/rss")
# checkNewFeed("https://www.theguardian.com/world/rss")
