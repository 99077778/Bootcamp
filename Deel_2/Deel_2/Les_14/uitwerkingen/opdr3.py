# Opdracht 3:
# Schrijf een programma dat een lijst van fruitsoorten maakt
# en vervolgens de gebruiker vraagt om een fruitsoort in te voeren. 
# Gebruik de remove functie om het opgegeven fruit uit de lijst 
# te verwijderen en print vervolgens de bijgewerkte lijst.



fruitlijst = ['appel','banaan','sinasappel','citroen','aardbei']
print(fruitlijst)

fruitinput = input('Vul een fruit die je uit de lijst wil verwijderen: ')


verwijderd_fruit = fruitlijst.remove(fruitinput)


    
    

print(f"Het verwijderde fruit is: {fruitinput}")
print(f"De bijgewerkte lijst is nu: {fruitlijst}")



