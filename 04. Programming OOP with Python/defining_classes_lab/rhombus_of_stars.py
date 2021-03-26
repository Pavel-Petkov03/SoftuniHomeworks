# Create a class called Cup. Upon initialization it should receive size and quantity (a number representing
# how much liquid is in it). The class should also have a method called fill(milliliters)
# which will increase the amount of liquid in the cup with the given milliliters (if there
# is space in the cup, otherwise ignore). The cup should also have a status() method which
# will return the amount of free space left in the cup. Submit only the class in the judge
# system. Don't forget to test your code.

def row(offset, multiplier):
    spaces = f'{offset * " "}'
    print(spaces + (' *' * multiplier).strip())


def create_rhombus(n):
    for i in range(1, n + 1):
        row((n - i), i)
    for i in range(n - 2, -1, -1):
        row((n - i - 1), (i + 1))


create_rhombus(int(input()))

