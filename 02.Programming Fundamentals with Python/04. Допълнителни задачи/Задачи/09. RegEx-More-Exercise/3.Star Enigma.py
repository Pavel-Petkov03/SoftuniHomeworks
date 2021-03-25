# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills.
# You are tasked to create a program to decrypt the messages of The Order and prevent the death of
# hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma.
# You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive and remove
# the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction)
# and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# •	The first line holds n – the number of messages– integer in range [1…100];
# •	On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.
import re
attacked = {}
destroyed = {}
pattern = r'@(?P<planet>[A-Z][a-z]+)([^@!:>-]?)+:(?P<population>\d+)([^@!:>-]?)+!(?P<attack_type>[AD])!([^@!:>-]?)+->(?P<soldier_count>\d+)'
times = int(input())
key_l = ['s','t','a','r']
for c in range(times):
	massage = input()
	count = len([c for c in massage if c.lower() in key_l])
	new_massage = ''.join([f'{chr(ord(c) - count)}' for c in massage])
	i = re.finditer(pattern, new_massage)
	for t in i:
		b = t.groupdict()
		if b['attack_type'] == 'A':
			attacked[b['planet']] = b['planet']
		else:
			destroyed[b['planet']] = b['planet']
print(f'Attacked planets: {len(attacked)}')
for key, value in sorted(attacked.items(), key=lambda x: x[0]):
	print(f'-> {key}')
print(f'Destroyed planets: {len(destroyed)}')
for key, value in sorted(destroyed.items(), key=lambda y: y[0]):
	print(f'-> {key}')

