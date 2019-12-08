from library import reference, rssProcess


def handleIndex():
    while 1:
        try:
            indexposition = input("Welchen wollen sie sich genauer ansehen? ")
            indexposition = int(indexposition)
            break
        except ValueError:
            print "Please enter only a indexposition that is valued. E.g. 5"
    return indexposition


page = reference.getList(reference._Guardian)

input_list = reference.inputToProcess("Was wuenschen Sie? ")

if reference.searchBy(input_list, reference.getList(reference.__Weather)):
    print ("Hier ist das aktuelle Wetter.")
elif reference.searchBy(input_list, reference.getList(reference.__News)):
    print ("Hier sind die aktuellen Top 5 News von " + page)
    print ("")
    rssProcess.show_all_Entries_of(page)
    if reference.followUp_handle("Wollen Sie sich einen genauer anschauen ? "):
        indexpos = int(handleIndex())
        rssProcess.full_feedEntry(page, indexpos)
elif reference.searchBy(input_list, reference.getList(reference.__Consent)):
    if reference.followUp_handle("Sind sie sicher? "):
        print ("Na gut")
    else:
        print ("Blop")
else:
    print ("Wie bitte ?")
