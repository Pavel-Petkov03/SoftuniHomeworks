from math import floor
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) is float:
            return cls(floor(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if type(value) is str and value.isdigit():
            return cls(int(value))
        return "wrong type"

    def add(self,integer):
        if type(integer) is Integer:
            return self.value + integer.value
        else:
            return "number should be an Integer instance"

