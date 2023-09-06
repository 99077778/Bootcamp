#Opdracht 2:
#Schrijf een programma met twee variabelen: 
# - a = 3
# - b = 7
#Bepaal met behulp van code welke variabele het hoogste getal is. 
#Je laat je programma kiezen welke van de drie meldingen moeten worden gestuurd:
#"Variabele a is het grootst want {waarde a} is groter dan {waarde b}"
#"Variabele b is het grootst want {waarde b} is groter dan {waarde a}"
#"Variabele a en b zijn gelijk."
#Test je programma door a en b een paar keer een andere waarde te geven.
#Als laatste stap laat je de gebruiker de getallen a en b invoeren. Zorg ervoor dat je programma goed blijft werken.


getalA = input("Voer een getal in voor A: ")
getalB = input("Voer een getal in voor B: ")


getalA = int(getalA)
getalB = int(getalB)


#print("test")


#result = getalA&getalB

#print("test", result)



if getalA > getalB:
    print(f"Variabele A is het grootst want {getalA} is groter dan {getalB}")
elif getalB > getalA:
    print(f"Variabele B is het grootst want {getalB} is groter dan {getalA}")
else:
    print("Variabele A en B zijn gelijk.")

# voor de laatste 6 regels heb ik google gebruikt