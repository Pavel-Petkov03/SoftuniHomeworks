# Да се напише програма, която чете текст (стринг),
# въведен от потребителя, и изчислява и отпечатва сумата от стойностите на гласните букви според
# таблицата по-долу:
# буква	a	e	i	o	u
# стойност	1	2	3	4	5
text = input()
sum = 0
for symbol in text:
    if symbol == "a":
        sum += 1
    elif symbol == "e":
        sum +=2
    elif symbol == "i":
        sum += 3
    elif symbol == "o":
        sum += 4
    elif symbol == "u":
        sum += 5
print(sum)
