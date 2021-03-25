# Да се напише програма, която чете число n, въведено от потребителя,
# и печата триъгълник от долари като в примерите:
symbol = "$"
rows = int(input())
for num in range(1, rows + 1):
    for i in range(num):
        print(symbol, end=" ")
    print('')



