# Opdracht 2:
# Schrijf een programma dat een lijst van 5 getallen maakt
# en vervolgens de gebruiker vraagt om een index in te voeren. 
# Gebruik de pop functie om het getal op de opgegeven index uit 
# de lijst te verwijderen en print vervolgens het verwijderde
# getal en de bijgewerkte lijst.






nummer_lijst = [1,2,3,4,5]


index = int(input("Voer een index in (0-4) om een getal te verwijderen: "))

if index < 0 or index >= len(nummer_lijst):
    print("Ongeldige index. Voer een index in tussen 0 en 4.")
else:
    
    verwijderd_getal = nummer_lijst.pop(index)
    

    print(f"Het verwijderde getal is: {verwijderd_getal}")
    print(f"De bijgewerkte lijst is nu: {nummer_lijst}")



