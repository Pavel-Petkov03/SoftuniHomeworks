
class vowels:
    VOWELS_SYMBOLS = 'aeouyi'

    def __init__(self, my_string):
        self.my_string = my_string
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.my_string):
            raise StopIteration

        value = self.start
        self.start += 1
        symbol = self.my_string[value]
        if symbol.upper() in vowels.VOWELS_SYMBOLS or symbol.lower() in vowels.VOWELS_SYMBOLS:
            return symbol
        return self.__next__()
