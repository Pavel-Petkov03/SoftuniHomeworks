# string = input()
# a = []
# for index in range(0 , len(string)):
#     if string[index].isupper():
#         a.append(index)
# print(a)


list1 = list(input())
for char in range(len(list1)):
    if 65 <= ord(list1[char]) <= 90:
        list1[char] = char
    else:
        list1.remove(list1[char])
print(list1)