# Opdracht 3.

# Schrijf een programma met de volgende functionaliteit:
# - vraag de gebruiker zijn naam in te voeren. 
# - vraag de gebruiker zijn leeftijd in jaren in te voeren. 

# Het programma 'print' (op het scherm via de terminal) vervolgens 1 van de volgende uitkomsten:
# - Beste <naam>, je bent nog geen 18. Alleen autorijden zit er dus niet in :-( 
# - Beste <naam>, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).

# Let op: Op de plek van <naam> toont het programma de ingevoerde naam.





naam = input("Vul je naam in: ")
jaar = input("Wat is je geboortejaar: ")

jaar = int(jaar)

if (jaar >= 2006):
    print("Beste " +naam+ " , je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ")
else:
    print('Beste ' +naam+ ', je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).')



