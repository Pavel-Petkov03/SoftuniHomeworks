def genrange(start, end):
    return (x for x in range(start, end+1))
print(list(genrange(1, 10)))