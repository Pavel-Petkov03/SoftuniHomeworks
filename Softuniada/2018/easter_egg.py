n = int(input())
width = 5 * n
height = 2 * n + 3
m = []
rower = 1
for i in range(n + 1):
    if i == 0 or i == height - 1:
        m.append(''.join(['*' if n * 2 <= el < n * 2 + n else '.' for el in range(width)]))
    elif 1 <= i <= n // 2:
        temp = []
        for el in range(width//2):
            # el > 2 * n - i * 2 + n + 2*i + i*2\
            # 3n + 2i
            # 20
            if el < 2 * n - 2 * i:
                temp.append('.')
            elif 2 * n - i * 2 <= el < 2 * n - i * 2 + i:
                temp.append('*')
            else:
                temp.append('+')
        temp = temp + list(reversed(temp))
        m.append(''.join(temp))
    else:
        temp = []
        for el in range(width // 2):
            if el < n - rower:
                temp.append('.')
            elif el < n - rower+ 2:
                temp.append('*')
            else:
                temp.append('=')
        temp = temp + list(reversed(temp))
        m.append(''.join(temp))
        rower += 1
# 2 * n - i * 2
happy_easter = 'HAPPY EASTER'
first_part = '.' * int(n/2) + '**'
second_part = '~' * int((width - (2 * len(first_part) + len(happy_easter))) // 2)
half = first_part + second_part
center = half + happy_easter + ''.join(reversed(list(half)))

[print(c) for c in m]
print(center)
[print(c) for c in reversed(m)]