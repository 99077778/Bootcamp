

# Vraag 10 getallen via de input.

# Nadat je 10 getallen hebt opgevraagd, doe je het volgende: 

# print: 
# het grootste getal is: ---
# het kleinste getal is: ---
# het aantal getallen deelbaar door 3 (zonder rest) is: ---
# hint:
# 9 % 3









getallen = []


for i in range(10):
    getal = int(input(f"Voer in getal {i + 1}: "))
    getallen.append(getal)



grootste_getal = max(getallen)
kleinste_getal = min(getallen)


aantal_deelbaar_door_3 = sum(1 for getal in getallen if getal % 3 == 0)






print(f"Het grootste getal is: {grootste_getal}")
print(f"Het kleinste getal is: {kleinste_getal}")
print(f"Het aantal getallen deelbaar door 3 (zonder rest) is: {aantal_deelbaar_door_3}")




