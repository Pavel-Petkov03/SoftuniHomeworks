quantity = int( input() )
days = int( input() )
price = 0
spirit = 0
for day in range( 1, days + 1 ):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        price += quantity * 2
        spirit += 5
    if day % 3 == 0:
        price += 8 * quantity
        spirit += 13
    if day % 5 == 0:
        spirit += 17
        price += quantity * 15
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        price += 23
        if days == day:
            spirit -= 30
print( f"Total cost: {price}" )
print( f'Total spirit: {spirit}' )
