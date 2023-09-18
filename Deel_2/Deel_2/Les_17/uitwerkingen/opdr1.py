# Opdracht 1:
# Raad het getal.
# Je gaat een eenvoudig raadspelletje maken. Hiervoor volg je een aantal stappen.
# 1. Maak een variabele aan en vul deze met een random getal tussen 1 en 5.
# 2. Vraag de gebruiker een getal in te voeren tussen 1 en 5.
# 3  a. Goed geraden: print dan in het groen: "Je hebt het getal goed geraden!"
#    b. Niet goed: print dan in het rood: "Je hebt het getal niet goed geraden!"


import random

random_getal = random.randint(1, 5)


input_getal = int(input("Raad het getal tussen 1 en 5: "))



if input_getal == random_getal:
    print("\033[92mJe hebt het getal goed geraden!\033[0m")
else:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m")


