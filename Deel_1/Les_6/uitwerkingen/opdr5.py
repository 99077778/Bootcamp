#Opdracht 5 (hard):
#Voer opdracht 2 nogmaals uit maar nu met 3 variabelen: a, b en c.
#Hint: je kunt dit in twee stappen uitvoeren.
#Vervolgens zorg je er ook weer voor dat de gebruiker de getallen kan invoeren.




getalA = input("Voer een getal in voor A: ")
getalB = input("Voer een getal in voor B: ")
getalC = input("Voer een getal in voor C: ")


getalA = int(getalA)
getalB = int(getalB)
getalC = int(getalC)



if getalA > getalB > getalC:
    print(f"Variabele A is het grootst, dan B, en daarna C. Want {getalA} is groter dan {getalB} en {getalC} is het kleinste getal.")
elif getalA > getalC > getalB:
    print(f"Variabele A is het grootst, dan C, en daarna B. Want {getalA} is groter dan {getalC} en {getalB} is het kleinste getal.")
elif getalC > getalB > getalA:
    print(f"Variabele C is het grootst, dan B, en daarna A. Want {getalC} is groter dan {getalB} en {getalA} is het kleinste getal.")
elif getalC > getalA > getalB:
    print(f"Variabele C is het grootst, dan A, en daarna B. Want {getalC} is groter dan {getalA} en {getalB} is het kleinste getal.")
elif getalB > getalC > getalA:
    print(f"Variabele C is het grootst, dan B, en daarna A. Want {getalB} is groter dan {getalC} en {getalA} is het kleinste getal.")
elif getalB > getalA > getalC:
    print(f"Variabele B is het grootst, dan A, en daarna C. Want {getalB} is groter dan {getalA} en {getalC} is het kleinste getal.")
elif getalA == getalB == getalC:
    print("Varriabele A, B en C zijn gelijk.")

else:
    print("2 van de 3 getallen zijn gelijk")


# had geen zin meer om if's te maken als er 2 getallen gelijk zijn