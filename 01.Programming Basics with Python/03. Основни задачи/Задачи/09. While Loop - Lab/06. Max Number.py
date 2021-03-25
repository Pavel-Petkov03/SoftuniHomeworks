import sys
# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя, и намира най-голямото измежду тях.
# Въвежда се по едно число на ред.
maximum = -sys.maxsize
num = input()
while num != "Stop":
    num = int(num)
    if num >= maximum:
        maximum = num
    num = input()
else:
    print(maximum)
