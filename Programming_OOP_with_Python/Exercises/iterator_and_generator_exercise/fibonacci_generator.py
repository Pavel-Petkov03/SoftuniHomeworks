def fibonacci():
    previous, current = 0, 1
    while True:
        yield previous
        previous, current = current, previous + current

generator = fibonacci()
for i in range(50):
    print(next(generator))


