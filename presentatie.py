def presenteer(mijn_dict, totaal):
    print("Invoer")
    for item, amount in mijn_dict.items():
        print(f"{item}: {amount}")
    print("=====================")
    print("Totaal:", totaal)
mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
totaal = 50
presenteer(mijn_dict, totaal) 
