# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100.
# You will be given a string, representing the working
# day events. Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number,
# separated by dash("{event/ingredient}-{number}")
# •	If the event is "rest": you gain energy, the number
# in the second part. But your energy cannot exceed your
# initial energy (100). Print: "You gained {0} energy.".
# After that, print your current energy: "Current energy: {0}.".
# •	If the event is "order": You've earned some coins, the
# number in the second part. Each time you get an order, your energy decreases with 30 points.
# o	If you have energy to complete the order, print: "You earned {0} coins.".
# o	If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case you are having an ingredient,
# you have to buy. The second part of the event, contains the coins you have to spent and remove from your coins.
# o	If you are not bankrupt (coins <= 0) you've bought
# the ingredient successfully, and you should print ("You bought {ingredient}.")
# o	If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the next three lines:
# "Day completed!", "Coins: {coins}", "Energy: {energy}".
# Input / Constraints
# You will receive a string, representing the working day
# events, separated with '|' (vertical bar): " event1|event2|event3…".
# Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")
# Output
# Print the corresponding messages, described above.
events = input().split("|")
energy = 100
max_energy = 100
coins = 100
order_energy = 30
rest_energy = 50
is_fine = True
for c in events:
    command, amount = c.split("-")
    amount = int(amount)
    if command == "rest":
        if energy + amount > max_energy:
            gained = max_energy - energy
            energy = max_energy
        else:
            gained = amount
            energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif command == "order":
        if energy >= order_energy:
            energy -= order_energy
            coins += amount
            print(f'You earned {amount} coins.')

        else:
            energy += rest_energy
            print("You had to rest!")
            continue

    else:
        if coins > amount:
            coins -= amount
            print(f"You bought {command}.")

        else:
            print(f'Closed! Cannot afford {command}.')
            is_fine = False
            break
if is_fine:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")


