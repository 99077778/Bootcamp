
# Opdracht 4:
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.





import random



aantal_rondes = 0
aantal_fouten = 0

while True:
    random_getal = random.randint(1, 5)
    aantal_rondes += 1
    print(f"\nRonde {aantal_rondes}")

    pogingen = 0

    while True:
        input_getal = int(input("Raad het getal tussen 1 en 5: "))
        pogingen += 1


        if input_getal == random_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            print(f"Je hebt {pogingen} poging(en) nodig gehad.")
            break
        else:
            print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw.\033[0m")
            aantal_fouten += 1

    speel_opnieuw = input("Wil je nog een ronde spelen? (ja/nee): ")
    if speel_opnieuw.lower() != "ja":
        break

print(f"\nAantal gespeelde rondes: {aantal_rondes}")
print(f"Aantal keer fout geraden: {aantal_fouten}")


