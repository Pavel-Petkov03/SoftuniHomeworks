# On the first line of the standard input you will receive an integer n – the number of heroes that you can
# choose for your party. On the next n lines, the heroes themselves will follow with their hit points and
# mana points separated by empty space in the following format:
# {hero name} {HP} {MP}
# -	where HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game.  You will be receiving
# different commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that can be performed by the heroes:
# CastSpell – {hero name} – {MP needed} – {spell name}
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# TakeDamage – {hero name} – {damage} – {attacker}
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# Recharge – {hero name} – {amount}
# •	The hero increases his MP. If a command is given that would bring the MP of the hero above the maximum value (200),
# MP is increased to 200. (the MP can’t go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# Heal – {hero name} – {amount}
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value
# (100), HP is increased to 100 (the HP can’t go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"
# Input
# •	On the first line of the standard input you will receive an integer n
# •	On the next n lines, the heroes themselves will follow with their hit points and mana points separated by
# empty space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
# •	Print all members of your party who are still alive, sorted by their HP in descending order, then by their
# name in ascending order, in the following format (their HP/MP need to be indented 2 spaces):
# "{hero name}
#  	 HP: {current HP}
#  MP: {current MP}
#  ..."
# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers, will never be negative or
# exceed the respective limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly
our_dict = {}
n = int(input())
for _ in range(n):
    name, h, m = input().split()
    our_dict[name] = [int(h), int(m)]
command = input()
while command != 'End':
    command = command.split(' - ')
    if len(command) == 3:
        _, hero_name, amount = command
        amount = int(amount)
        if _ == 'Recharge':
            if our_dict[hero_name][1] + amount > 200:
                gain = 200 - our_dict[hero_name][1]
            else:
                gain = amount
            print(f"{hero_name} recharged for {gain} MP!")
            our_dict[hero_name][1] += gain
        elif _ == 'Heal':
            if our_dict[hero_name][0] + amount > 100:
                gain = 100 - our_dict[hero_name][0]
            else:
                gain = amount
            print(f"{hero_name} healed for {gain} HP!")
            our_dict[hero_name][0] += gain
    elif len(command) == 4:
        _, hero_name, dmg_or_mana, spell_or_attacker = command
        if _ == 'CastSpell':
            mana = int(dmg_or_mana)
            spell = spell_or_attacker
            if our_dict[hero_name][1] >= mana:
                print(f"{hero_name} has successfully cast {spell} and now has {our_dict[hero_name][1] - mana} MP!")
                our_dict[hero_name][1] -= mana
            else:
                print(f"{hero_name} does not have enough MP to cast {spell}!")
        elif _ == 'TakeDamage':
            dmg = int(dmg_or_mana)
            attacker = spell_or_attacker
            if dmg >= our_dict[hero_name][0]:
                print(f"{hero_name} has been killed by {attacker}!")
                our_dict.pop(hero_name)
            else:
                print(
                    f"{hero_name} was hit for {dmg} HP by {attacker} and now has {our_dict[hero_name][0] - dmg} HP left!")
                our_dict[hero_name][0] -= dmg

    command = input()

for key, value in sorted(our_dict.items(), key=lambda x: (-x[1][0], x[0])):
    print(f'{key}\n  HP: {value[0]}\n  MP: {value[1]}')
