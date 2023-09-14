# Opdracht 4:
# Schrijf een programma dat een lege lijst maakt en vervolgens de
# gebruiker vraagt om 5 woorden in te voeren. Gebruik de append
# functie om elk woord aan de lijst toe te voegen en gebruik 
# vervolgens een for-lus om door elk woord in de lijst te itereren
# en print elk woord op een aparte regel.

nummer_lijst = []


nummer1 = int(input("Voer een eerste nummer in: "))
nummer2 = int(input("Voer een tweede nummer in: "))
nummer3 = int(input("Voer een derde nummer in:  "))
nummer4 = int(input("Voer een vierde nummer in: "))
nummer5 = int(input("Voer een vijfde nummer in: "))

nummer_lijst.append(nummer1)
nummer_lijst.append(nummer2)
nummer_lijst.append(nummer3)
nummer_lijst.append(nummer4)
nummer_lijst.append(nummer5)



for nummer in nummer_lijst:
    print(nummer)

