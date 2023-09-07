# Opdracht 1:
# In Nederland krijg je op school regelmatig een cijfer.
# Wist je dat bij die cijfers ook een omschrijving hoort? 
# Schrijf jij een programma wat de juiste omschrijving print bij een cijfer.

# Houd rekening met het volgende:
# Je schrijft een programma met 1 variabele: cijfer. Dit cijfer gebruik je om de omschrijving te printen:

# Cijfer	Omschrijving
# 10	uitmuntend
# 9	zeer goed
# 8	goed
# 7	ruim voldoende
# 6	voldoende
# 5	bijna voldoende
# 4	onvoldoende
# 3	gering
# 2	slecht
# 1	zeer slecht





cijfer = input('vul je cijfer in: ')

cijfer = int(cijfer)


if cijfer == 10:
    print("uitmuntend")
elif cijfer == 9:
    print("zeer goed")
elif cijfer == 8:
    print("goed")
elif cijfer == 7:
    print("ruim voldoende")
elif cijfer == 6:
    print("voldoende")
elif cijfer == 5:
    print("bijna voldoende")
elif cijfer == 4:
    print("onvoldoende")
elif cijfer == 3:
    print("gering")
elif cijfer == 2:
    print("slecht")
elif cijfer == 1:
    print("zeer slecht")
else:
    print("ongeldig cijfer")






