# Напишете програма, която чете цяло положително число n, въведено от потребителя,
# и печата числата от n до 1 в обратен ред (от най-голямото към най-малкото).
n = int(input())
for i in reversed(range(1, n + 1)):
    print(i)