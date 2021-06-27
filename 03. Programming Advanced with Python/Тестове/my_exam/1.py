from collections import deque

milkshake = 0
choco = list(map(int, input().split(', ')))
milks = deque([int(c) for c in input().split(', ')])
while choco and milks:
    if choco[-1] <= 0 or milks[0] <= 0:
        if choco[-1] <= 0:
            choco.pop()
        if milks[0] <= 0:
            milks.popleft()
        continue

    if choco[-1] == milks[0]:
        choco.pop()
        milks.popleft()
        milkshake += 1
    else:
        milks.append(milks.popleft())
        choco[-1] -= 5
    if milkshake == 5:
        break

if milkshake == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")
if choco:
    print(f"Chocolate: {', '.join([str(c) for c in choco])}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join([str(c) for c in milks])}")
else:
    print("Milk: empty")
