# Opdracht 2:
# Oh ja: we (oefenen het) formatteren het ook nog even netjes:
# Is je cijfer 6 of groter dan print je:
# "Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}"

# Heb je lager dan een 6 gescoord dan wordt het: 
# "Jammer, {omschrijving} je resultaat is een {cijfer}"

# Zorg ervoor dat een gebruiker een cijfer tussen 1 en 10 kan invoeren. 
# Wordt het getal te groot of te klein dan moet je een melding geven: 'Dit kan ik niet omzetten!'





cijfer = input('vul je cijfer in: ')

cijfer = int(cijfer)

omschrijving = ""




if cijfer >= 6:
    if cijfer == 10:
        omschrijving = "je hebt een uitmuntend cijfer gehaald"
    elif cijfer == 9:
        omschrijving = "je hebt een zeer goed cijfer gehaald"
    elif cijfer == 8:
        omschrijving = "je hebt een goed cijfer gehaald"
    elif cijfer == 7:
        omschrijving = "je hebt een ruim voldoende gehaald"
    elif cijfer == 6:
        omschrijving = "je hebt een voldoende gehaald"
    else:
        omschrijving = "Dit kan ik niet omzetten!"
else:
    if cijfer == 5:
        omschrijving = "bijna voldoende,"
    elif cijfer == 4:
        omschrijving = "onvoldoende,"
    elif cijfer == 3:
        omschrijving = "gering,"
    elif cijfer == 2:
        omschrijving = "slecht,"
    elif cijfer == 1:
        omschrijving = "zeer slecht,"
    else:
        omschrijving = "Dit kan ik niet omzetten!"

if omschrijving:
    if cijfer >= 6:
        print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
    else:
        print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")








# Andere makkelijkere manier



# cijfer = input('vul je cijfer in: ')

# cijfer = int(cijfer)


# if cijfer == 10:
#     print("Gefeliciteerd, je hebt een uitmuntend cijfer gehaald je resultaat is een 10")
# elif cijfer == 9:
#     print("Gefeliciteerd, je hebt een zeer goed cijfer gehaald je resultaat is een 9")
# elif cijfer == 8:
#     print("Gefeliciteerd, je hebt een goed cijfer gehaald je resultaat is een 8")
# elif cijfer == 7:
#     print("Gefeliciteerd, je hebt een ruim voldoende gehaald je resultaat is een 7")
# elif cijfer == 6:
#     print("Gefeliciteerd, je hebt een voldoende gehaald je resultaat is een 6")
# elif cijfer == 5:
#     print("Jammer, bijna voldoende, je resultaat is een 5")
# elif cijfer == 4:
#     print("Jammer, onvoldoende, je resultaat is een 4")
# elif cijfer == 3:
#     print("Jammer, gering, je resultaat is een 3")
# elif cijfer == 2:
#     print("Jammer, slecht, je resultaat is een 2")
# elif cijfer == 1:
#     print("Jammer, zeer slecht, je resultaat is een 1")
# else:
#     print("ongeldig cijfer")

