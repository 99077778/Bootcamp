

# length = len('aap noot mies')

# print(length)

# print(len('aap noot mies')*12)


def product(getal1, getal2, operator):
    if operator == "/":
        result = getal1 / getal2
    elif operator == "*":
        result = getal1 * getal2
    else:
        result = 0
    return result







# def divide(getal1, getal2):
#     result = (getal1 * getal2)
#     return result








def operate(getal1, getal2, operator):
    



g1 = int(input('getal 1: '))
g2 = int(input('getal 2: '))

op = input('operator: ')

print(product(g1, g2, op))



