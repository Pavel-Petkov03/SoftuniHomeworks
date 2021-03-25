# You will receive a single number. You have to write a function that returns the sum of all even and all
# odd digits from that number as a single string like in the examples below.
def convert(text):
    odd = 0
    even = 0
    for index in range(len(text)):
        if int(text[index]) % 2 == 0:
            even += int(text[index])
        else:
            odd += int(text[index])
    return f' Odd sum = {odd}, Even sum = {even}'


initial_text = input()

print(convert(initial_text))

