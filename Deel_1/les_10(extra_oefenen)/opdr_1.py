

# Cijfers voor proefwerken en tentamens vallen tussen nul en 10 (inclusief nul en 10),
# en worden altijd afgerond op halve punten.

# De Amerikaanse stijl van beoordelen gebruikt letters.

# Ter vergelijking,de cijfers 8.5 tot en met 10 zijn in
# Amerika “A,” 7.5 en 8 zijn “B," 6.5 en 7 zijn “C,” 5.5 en 6 zijn “D,” en 5 en lager is “F.”
 

# Schrijf code die deze vertaling van cijfers naar letters maakt,
# waarbij de gebruiker gevraagd wordt om het cijfer in te geven.
# Als de gebruiker een cijfer buiten het gegeven bereik ingeeft, moet je een foutmelding geven.






cijfer = float(input("Voer een cijfer in tussen 0 en 10: "))



if 0 <= cijfer <= 10:


    afgerond_cijfer = round(cijfer * 2) / 2
    

    
    if 8.5 <= afgerond_cijfer <= 10:
        beoordeling = "A"
    elif 7.5 <= afgerond_cijfer < 8.5:
        beoordeling = "B"
    elif 6.5 <= afgerond_cijfer < 7.5:
        beoordeling = "C"
    elif 5.5 <= afgerond_cijfer < 6.5:
        beoordeling = "D"
    else:
        beoordeling = "F"

   

    print(f"De beoordeling voor {cijfer} is een {beoordeling}")
else:
    print("Verkeerde cijver ingevuld")







