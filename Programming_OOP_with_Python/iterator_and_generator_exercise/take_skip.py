class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        self.counter += 1
        self.result = self.value
        self.value += self.step
        return self.result

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

