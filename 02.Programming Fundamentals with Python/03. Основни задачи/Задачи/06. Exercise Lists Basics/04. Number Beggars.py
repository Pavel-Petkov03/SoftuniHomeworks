# Your task here is pretty simple: given a list of numbers and a number of beggars,
# you are supposed to return a list with the sum of what each beggar brings home,
# assuming they all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5],
# the second collects [2,4].
# The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3, as they will
# respectively take [1, 4], [2, 5] and [3].
# Also note that not all beggars have to take the same amount of "offers", meaning that the length of the
# list is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will
# of course take nothing (0).
# Input
# You will receive 2 lines of input: a single string containing the numbers separated by a comma and a
# space ", ". On the second line you will receive the number of beggars.
# Output
# Print a list of all the sums that each beggar got.
initial = input().split(",")
beggars = int(input())
new = []
final = []
all_sum = 0
for i in range(len(initial)):
    new.append(int(initial[i]))
if len(new) == beggars:
    final = new
elif len(new) < beggars:
    final = new
    n = beggars - len(new)
    for c in range(1 , n + 1):
        final.append(0)
else:
    for beggar in range(0,  beggars): # beggar = 0 защото трябва втория фор цикъл да започва с 0 за да обходя листа
        for b in range(beggar,len(new),beggars):
            if b > len(new):
                break
            else:
                all_sum += new[b]
        final.append(all_sum)
        all_sum = 0
print(final)




