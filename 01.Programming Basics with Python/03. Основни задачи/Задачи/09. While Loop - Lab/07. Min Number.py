import sys
# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя, и намира най-голямото измежду тях.
# Въвежда се по едно число на ред.
minimum = sys.maxsize
num = input()
while num != "Stop":
    num = int(num)
    if num <= minimum:
        minimum = num
    num = input()
else:
    print(minimum)




