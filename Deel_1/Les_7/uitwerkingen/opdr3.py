#Opdracht 3: 
#Bereken met een while loop hoeveel keer 25 in 625 past.
#(Let op: max. 8 regels code!)




# totaal = 625
# delingsgetal = 25


# aantal_keer = totaal // delingsgetal


# print(f"{delingsgetal} past {aantal_keer} keer in {totaal}.")





totaal = 625
delingsgetal = 25
aantal_keer = 0

while totaal >= delingsgetal:
    totaal -= delingsgetal
    aantal_keer += 1

print(f"{delingsgetal} past {aantal_keer} keer in {totaal}.")
