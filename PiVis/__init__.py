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

while 1:
    input_list = reference.inputToProcess("Was wuenschen Sie? ")

    if reference.searchBy(input_list, reference.getList(reference.__Weather)):
        print ("Hier ist das aktuelle Wetter.")
    elif reference.searchBy(input_list, reference.getList(reference.__News)):
        print ("Hier sind die aktuellen Top 5 News von " + page)
        print ("")
        rssProcess.show_all_Entries_of(page)
        while reference.followUp_handle("Wollen Sie sich einen genauer anschauen ? "):
            indexpos = int(handleIndex())
            rssProcess.full_feedEntry(page, indexpos)
    elif reference.searchBy(input_list, reference.getList(reference.__Note)):
        while reference.followUp_handle("Wollen Sie eine Erinnerung setzen, Sir ? "):
            __newNote = input("Wie lautet ihre neue Notiz ?")
            reference.__Notelist.append(__newNote)
        if reference.followUp_handle("Wollen Sie ihre aktuellen Erinnerungen auslesen ? "):
            for x in range(0, len(reference.__Notelist)):
                print ("[" + str(x) + "] " + reference.__Notelist[x])
                x = x + 1
        while reference.followUp_handle("Wollen Sie eine der Notizen entfernen ? "):
            __delete = input("Welche Notiz soll entfernt werden ? Geben Sie bitte die Indexposition an. ")
            print (reference.__Notelist.pop(__delete) + " wurde entfernt.")
        __newrow = ",".join(reference.__Notelist)
        reference.rewrite_csv("library/csv/Notes.csv", __newrow)
    else:
        print ("Wie bitte ?")
