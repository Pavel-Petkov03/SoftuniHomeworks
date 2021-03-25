# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list
a = input().split(", ")
new = []
for c in range(len(a)):
    new.append(int(a[c]))
for d in range(len(new)):
    if new[d] == 0:
        new.remove(new[d])
        new.append(0)
print(new)