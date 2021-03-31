# You are given a secret message you need to decipher.
# Here are the things you need to know to decipher it:
# For each word:
# •	the second and the last letter are switched (e.g. Hello becomes Holle)
# •	the first letter is replaced by its character code (e.g. H becomes 72)
text = input().split()


def swap(c):
    c[1], c[-1] = c[-1], c[1]
    return "".join(c)


res = []

for key in text:
    list_of_str = []
    first_list = [i for i in key if i.isdigit()]
    list_of_str.insert(0, chr(int("".join(first_list))))
    [list_of_str.append(j) for j in key if not j.isdigit()]

    res.append(swap(list_of_str))
    first_list.clear()
    list_of_str.clear()

res = " ".join(res)

print(res)
