aantal_studenten = 23

collegegeld_per_student = 2000
totaal_collegegeld = aantal_studenten * collegegeld_per_student

prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95


btw_percentage = 9


totaal_fruitprijs = prijs_appels + prijs_druiven + prijs_bananen


btw_bedrag = (totaal_fruitprijs * btw_percentage) / 100


totaal_bedrag_inclusief_btw = totaal_fruitprijs + btw_bedrag

print(f"Totaalbedrag aan collegegeld voor {aantal_studenten} studenten: {totaal_collegegeld} euro")
print(f"Totaalbedrag voor de fruitmand zonder BTW: {totaal_fruitprijs} euro")
print(f"BTW-bedrag voor de fruitmand ({btw_percentage}%): {btw_bedrag} euro")
print(f"Totaalbedrag voor de fruitmand inclusief BTW: {totaal_bedrag_inclusief_btw} euro")
