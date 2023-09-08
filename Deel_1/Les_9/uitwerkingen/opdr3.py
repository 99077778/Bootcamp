# Opdracht 3:
# Schrijf een programma met 3 variabelen:
# leeftijd = 18, snor = j (of n) en diploma = j (of n).

# Je schrijft een programma wat bepaalt of iemand is aangenomen. 
# Je bent aangenomen als je: 18 bent (of ouder) en een snor hebt of onder de 18 met een diploma.

# Let op:
# Je mag maar 1 if statement gebruiken!!!

# Test je programma door de variabelen te wijzigen.







leeftijd = input("Voer je leeftijd in: ")

leeftijd = int(leeftijd)



snor = input("Heb je een snor? Voer 'ja' of 'nee' in: ")

diploma = input("Heb je een diploma? Voer 'ja' of 'nee' in: ")



if (leeftijd >= 18 and snor == "ja") or (leeftijd < 18 and diploma == "ja"):
    print("je bent aangenomen")
else:
    print("je bent niet aangenomen")



