#Opdracht 3:
#Definieer drie variabelen var1, var2 en var3. Bereken het gemiddelde en
#stop het in een variabele gemiddelde. Toon het gemiddelde. Voeg drie commentaren toe.
#Pas het programma nu zo aan dat de gebruiker getallen kan invoeren.



var1 = input("Vul een getal in: ")
var2 = input("Vul een 2e getal in: ")
var3 = input("Vul een 3e getal in: ")


# text omzetten naar getallen
var1 = int(var1)
var2 = int(var2)
var3 = int(var3)



print(var1+var2+var3)



result = var1+var2+var3


#gemiddelde berekenen
aantal_getallen = 3
gemiddelde = result / aantal_getallen

print("De som van de ingevoerde getallen is:", result)
print("Het gemiddelde van de ingevoerde getallen is:", gemiddelde)



#voor die gemmidelde berekenen had ik google gebruikt