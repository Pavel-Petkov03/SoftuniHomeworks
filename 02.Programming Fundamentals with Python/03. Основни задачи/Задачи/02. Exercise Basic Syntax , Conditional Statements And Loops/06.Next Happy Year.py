year = input()
while True:
    year = str(int(year) + 1)
    if len(set(year)) == len(year):
        print(year)
        break


