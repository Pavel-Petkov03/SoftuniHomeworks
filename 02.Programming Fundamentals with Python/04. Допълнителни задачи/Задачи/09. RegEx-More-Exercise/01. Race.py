import re
names = input().split(", ")
our_dict = {}
pattern_name = r'[A-Za-z]+'
pattern_km = r'\d'
command = input()
while command != 'end of race':
	name = "".join([c.group() for c in re.finditer(pattern_name, command)])
	km = sum([int(c.group()) for c in re.finditer(pattern_km, command)])
	if name in names:
		if name in our_dict:
			our_dict[name] += km
		else:
			our_dict[name] = km
	command = input()
result = []
for player, max_p in sorted(our_dict.items(), key=lambda x: -x[1]):
	if len(result) <= 3:
		result.append([player, max_p])
	else:
		break
for times in range(0, 3):
	if times == 0:
		print(f'1st place: {result[times][0]}')
	elif times == 1:
		print(f'2nd place: {result[times][0]}')
	elif times == 2:
		print(f'3rd place: {result[times][0]}')