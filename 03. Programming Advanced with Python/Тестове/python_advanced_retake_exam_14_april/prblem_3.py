def flights(*args):
    final = {}
    index = 0
    while args[index] != 'Finish':
        if args[index] not in final:
            final[args[index]] = 0
        final[args[index]] += int(args[index+1])
        index += 2
    return final


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))