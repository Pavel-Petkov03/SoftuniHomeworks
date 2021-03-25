word = input()
i = len(word) - 1
symbol = ''
while i >= 0:
    symbol += word[i]
    i -= 1
print(symbol)

