a = input().split()
b = input().split()
c = input().split()
is_first = False
is_second = False
is_digit = None
if a[0] == a[1] == a[2]:
    is_digit = a[0]
elif b[0] == b[1] == b[2]:
    is_digit = b[0]
elif c[0] == c[1] == c[2]:
    is_digit = c[0]
elif a[0] == b[0] == c[0]:
    is_digit = a[0]
elif a[1] == b[1] == c[1]:
    is_digit = a[1]
elif a[2] == b[2] == c[2]:
    is_digit = a[2]
elif a[0] == b[1] == c[2]:
    is_digit = a[0]
elif c[0] == b[1] == a[2]:
    is_digit = a[2]
if is_digit == "1":
    print("First player won")
elif is_digit == "2":
    print("Second player won")
else:
    print("Draw!")