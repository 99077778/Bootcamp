# Opdracht 1:
# Pak opdracht 3 van gisteren.
# Kijk eens naar de functies: get_integer en get_float.
# Voer hier eens een string (bijv.: zes) in! Wat gebeurt er?
# Los dit probleem op met een try en except.

# Let op: Zorg ervoor dat je net zolang om een getal vraagt tot de
# gebruiker een geldig getal heeft ingevoerd.





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

