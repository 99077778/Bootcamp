# Opdracht 3:
# Je gaat een hulpmiddel schrijven die je bij het programmeren kunt gebruiken. 
# Maak de file: user_input.py.

# Hierin schrijf je de volgende functies:
# - get_integer()
# krijgt één string parameter, de prompt, en vraagt de gebruiker via
# die prompt om een integer in te geven. De functie retourneert een integer.


# - get_float() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om een float in te geven. De functie retourneert een float.

# - getString() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om een string in te geven. Alles wat de gebruiker ingeeft wordt als correct
# beschouwd. De functie retourneert de ingevoerde waarde als string.

# - get_letter() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om één letter in te geven. Alleen letters van het alfabet zijn acceptabel.
# Pas als de gebruiker precies één letter heeft ingegeven eindigt de functie, 
# en de letter wordt dan als een hoofdletter geretourneerd.





def get_integer(prompt):
    while True:
        try:
            integer_input = int(input(prompt))
            return integer_input
        except ValueError:
            print("Ongeldige invoer. Voer een integer in.")

def get_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))
            return float_input
        except ValueError:
            print("Ongeldige invoer. Voer een float in.")

def get_string(prompt):
    return input(prompt)

def get_letter(prompt):
    while True:
        letter = input(prompt).strip()
        if len(letter) == 1 and letter.isalpha():
            return letter.upper()
        else:
            print("Ongeldige invoer. Voer precies één letter van het alfabet in.")

