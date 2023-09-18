# Opdracht 2:
# Breid je programma nu zodanig uit dat de gebruiker net zolang
# moet raden tot hij het juiste getal heeft gevonden.




import random

random_getal = random.randint(1, 5)



while True:
    input_getal = int(input("Raad het getal tussen 1 en 5: "))

    
    if input_getal == random_getal:
        print("\033[92mJe hebt het getal goed geraden!\033[0m")
        break
    else:
        print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw.\033[0m")

