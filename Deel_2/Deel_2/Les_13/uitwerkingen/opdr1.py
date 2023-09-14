# Opdracht 1:
# Maak een tuple met een lijst kleuren.
# Schrijf code die de gebruiker vraagt om hun naam en favoriete kleur. 
# Controleer of de favoriete kleur van de gebruiker in de tuple voorkomt. 

# Is dat het geval: print klein verhaaltje met daarin de naam naam en kleur.
# Anders print je: "Deze kleur is niet zo geweldig!"



kleur = ('geel','groen','rood','blauw','oranje')

a = input('Wat is je naam? ')

b = input('Vul een kleur in: ')




if b in kleur:
    print(f'Hallo {a} je hebt een goede kleur ingevuld {b} is een mooie kleur')
else:
    print('Deze kleur is niet zo geweldig!')











# autos = ('fiat','bmw','mercedes','volkswagen','jaguar')
# print('We hebben meerdere occasions')
# for aanbieding in autos:
#     print(aanbieding)


# auto = input('Wat wilt u kopen? ')

# if auto in autos:
#     print('Wat biedt u?')
# else:
#     print('Helaas, daar valt niets aan te verdienen!')



# print(autos[2])

