#Opdracht 3:
#Schrijf een programma met één variabele: leeftijd.
#Als de waarde van de variabele 16 of hoger is print je: 
#"Gefeliciteerd, je mag je brommerrijbewijs halen." 
#Anders print je:
#"Helaas, je zult nog even moeten wachten."

#Test je programma door alleen de variabele leeftijd een andere waarde te geven. 
#Test ook eens met 16.



leeftijd = input("vul hier je leeftijd in: ")

leeftijd = int(leeftijd)


if leeftijd >= 16:
    print("Gefeliciteerd, je mag je brommerrijbewijs halen.")
else:
    print("Helaas, je zult nog even moeten wachten.")
