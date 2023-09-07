# Opdracht 4:
# Neem je programma van opdracht 3. 
# Gebruik het nu om uit te rekenen hoeveel keer 12 in 625 past.
# Moest je hier nog iets voor aanpassen (behalve dan wat cijfers)? 
# (Let op: ook dit kan in max. 8 regels code!)






# totaal = 625
# delingsgetal = 12


# aantal_keer = totaal // delingsgetal


# print(f"{delingsgetal} past {aantal_keer} keer in {totaal}.")





totaal = 625
delingsgetal = 12
aantal_keer = 0

while totaal >= delingsgetal:
    totaal -= delingsgetal
    aantal_keer += 1

print(f"{delingsgetal} past {aantal_keer} keer in {totaal}.")



# Moest je hier nog iets voor aanpassen (behalve dan wat cijfers)?  Nee
