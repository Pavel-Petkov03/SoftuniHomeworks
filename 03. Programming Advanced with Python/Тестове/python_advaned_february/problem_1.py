from collections import deque

fireworks_effect = deque(map(int, input().split(', ')))
explosive_power = list(map(int, input().split(', ')))


def check(dect):
    for c in dect.values():
        if c < 3:
            return False
    return True



count_dict = {
    'palm': 0,
    'willow': 0,
    'crosette': 0,
}
while fireworks_effect and explosive_power and not check(count_dict):
    if fireworks_effect[0] <= 0:
        fireworks_effect.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    val = fireworks_effect[0] + explosive_power[-1]
    if val % 3 == 0 and val % 5 != 0:
        count_dict['palm'] += 1

        fireworks_effect.popleft()
        explosive_power.pop()
    elif val % 3 != 0 and val % 5 == 0:
        count_dict['willow'] += 1
        fireworks_effect.popleft()
        explosive_power.pop()
    elif val % 3 == 0 and val % 5 == 0:
        fireworks_effect.popleft()
        count_dict['crosette'] += 1
        explosive_power.pop()
    else:
        fireworks_effect[0] -= 1
        fireworks_effect.append(fireworks_effect.popleft())

print("Congrats! You made the perfect firework show!" if check(
    count_dict) else "Sorry. You can't make the perfect firework show.")
if fireworks_effect:
    print(f"Firework Effects left: {', '.join([str(c) for c in fireworks_effect])}")
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(c) for c in explosive_power])}')
print(f"Palm Fireworks: {count_dict['palm']}")
print(f"Willow Fireworks: {count_dict['willow']}")
print(f"Crossette Fireworks: {count_dict['crosette']}")
