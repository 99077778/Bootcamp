# Opdracht 3:
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer
# een getal moet worden geraden.




import random

aantal_rondes = 3



for ronde in range(aantal_rondes):
    random_getal = random.randint(1, 5)
    print(f"\nRonde {ronde + 1} van de {aantal_rondes}")

    while True:
        input_getal = int(input("Raad het getal tussen 1 en 5: "))


        if input_getal == random_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            break
        else:
            print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw.\033[0m")


