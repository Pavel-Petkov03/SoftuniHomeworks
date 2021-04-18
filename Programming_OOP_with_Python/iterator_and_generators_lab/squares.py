def squares(num):
    return (c**2 for c in range(1, num+1))
print(list(squares(5)))

