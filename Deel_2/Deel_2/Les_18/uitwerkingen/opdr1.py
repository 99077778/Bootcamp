# Opdracht 1:
# je spel (van de vorige les) wordt een hit.
# Gebruikers klagen alleen dat het erg lang duurt voordat ze klaar zijn met raden.
# Na diepgravend onderzoek kom er achter dat je nergens meldt in welke range men kan raden en gebruikers 
# blijken dus te denken dat ze tussen 1 en 100 mogen raden.

# Breid je gereedschap uit met een functie die kan controleren of de ingevoerde waarde in een lijst voorkomt. 
# Je kunt deze functie op twee plaatsen inzetten. Waar? En doe dit dan ook.



import random



def is_binnen_range(getal, min_waarde, max_waarde):
    return min_waarde <= getal <= max_waarde


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


        if not is_binnen_range(input_getal, 1, 5):
            print("\033[91mHet ingevoerde getal moet tussen 1 en 5 zijn.\033[0m")
            continue


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


