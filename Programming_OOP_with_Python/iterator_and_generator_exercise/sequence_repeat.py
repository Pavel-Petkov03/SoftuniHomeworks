class sequence_repeat:
    def __init__(self, seq, all_letters):
        self.sequence = seq
        self.letters = all_letters
        self.counter = 0
        self.index = 0

    def __next__(self):
        if self.letters == self.counter:
            raise StopIteration
        value = self.sequence[self.index]
        self.index += 1
        self.counter += 1
        if self.index == len(self.sequence):
            self.index = 0
            return self.sequence[-1]
        return value

    def __iter__(self):
        return self

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

