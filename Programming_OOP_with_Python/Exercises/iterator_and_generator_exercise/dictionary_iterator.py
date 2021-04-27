class dictionary_iter:
    def __init__(self, dect):
        self.dect = [(key, value) for key, value in dect.items()]
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > len(self.dect) - 1:
            raise StopIteration
        value = self.dect[self.start]
        self.start += 1
        return value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
