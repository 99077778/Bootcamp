# Opdracht 1:
# Schrijf een programma dat een lege lijst maakt en
# vervolgens de gebruiker vraagt om 5 getallen in te voeren.
# Gebruik de append functie om elk getal aan de lijst 
# toe te voegen en print vervolgens de lijst.



nummer_lijst = []


nummer1 = int(input("Voer een eerste nummer in: "))
nummer2 = int(input("Voer een tweede nummer in: "))
nummer3 = int(input("Voer een derde nummer in: "))
nummer4 = int(input("Voer een vierde nummer in: "))
nummer5 = int(input("Voer een vijfde nummer in: "))

nummer_lijst.append(nummer1)
nummer_lijst.append(nummer2)
nummer_lijst.append(nummer3)
nummer_lijst.append(nummer4)
nummer_lijst.append(nummer5)


print(nummer_lijst)

