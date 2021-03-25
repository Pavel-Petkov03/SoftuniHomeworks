# Напишете програма, която чете цяло положително золата правоъгълник от n * n звездички.
stars = "*"
num = int(input())
for c in range(1 , num + 1):
    print(stars * num)