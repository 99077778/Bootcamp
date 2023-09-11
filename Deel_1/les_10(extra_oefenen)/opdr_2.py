# Opdracht
# Maak een programma die de gebruiker om een getal vraagt.

# Aan de hand van het getal dat de gebruiker invoert telt het programma naar 0. 

# Dus bij een invoer van 4 krijgt de gebruiker te zien:

# 4
# 3
# 2
# 1
# 0

# Maar bij het invoeren van -4 krijgt de gebruiker te zien:

# -4
# -3
# -2
# -1
# 0





getal = input("Voer een getal in: ")

getal = int(getal)



import time

if getal > 0:
    for i in range(getal, -1, -1):
        print(i)
        time.sleep(1)


elif getal < 0:
    for i in range(getal, 1):
        print(i)
        time.sleep(1)


else:
    print(0)
























