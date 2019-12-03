from library import reference

recent_input = input("Was wuenschen Sie ?")

input_list = recent_input.split(" ")

if reference.searchBy(reference.getList(reference.__Weather)) in input_list:
    print ("Hier ist das aktuelle Wetter.")
elif reference.searchBy(reference.getList(reference.__News)) in input_list:
    print ("Hier sind die aktuellen News.")
else:
    print ("Wie bitte ?")
