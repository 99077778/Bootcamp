# Opdracht 2:
# Schrijf een programma dat de gebruiker vraagt om twee getallen in te voeren.
# Gebruik vervolgens typecasting om de getallen om te zetten in floats 
# en bereken het gemiddelde van de twee getallen.



getal1 = input('Voer een getal in: ')
getal2 = input('Voer nog een getal in: ')

getal1 = float(getal1)
getal2 = float(getal2)

# uitkomst = float(uitkomst)

uitkomst = getal1 + getal2 / 2


print('Het gemiddelde van de twee getallen is ' + str(uitkomst))


