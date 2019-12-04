from library import reference, newsProcess

page = "https://www.theguardian.com/world/rss"

recent_input = input("Was wuenschen Sie ?")

input_list = recent_input.split(" ")

if reference.searchBy(input_list, reference.getList(reference.__Weather)):
    print ("Hier ist das aktuelle Wetter.")
elif reference.searchBy(input_list, reference.getList(reference.__News)):
    print ("Hier sind die aktuellen News.")
    print ("")
    newsProcess.show_5_Entries_of(page)
else:
    print ("Wie bitte ?")
