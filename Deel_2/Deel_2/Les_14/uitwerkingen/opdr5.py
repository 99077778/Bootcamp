# Opdracht 5:
# Schrijf een programma dat een lijst van 5 namen maakt 
# en vervolgens de gebruiker vraagt om een naam in te voeren. 

# Gebruik de remove functie om de opgegeven naam uit de lijst 
# te verwijderen als deze voorkomt en print vervolgens de
# bijgewerkte lijst. Als de opgegeven naam niet in de lijst voorkomt,
# gebruik dan de append functie om deze aan de lijst toe te
# voegen en print vervolgens de bijgewerkte lijst.




fruitlijst = ['appel','banaan','sinasappel','citroen','aardbei']
print(fruitlijst)

fruitinput = input('Vul een fruit die je uit de lijst wil verwijderen of vul een fruit eraan toe: ')



if fruitinput in fruitlijst:
    fruitlijst.remove(fruitinput)
    print(f"Het verwijderde fruit is: {fruitinput}")
else:
    fruitlijst.append(fruitinput)
    print(f"{fruitinput} is aan de lijst toegevoegd.")


print(f"De bijgewerkte lijst is nu: {fruitlijst}")



