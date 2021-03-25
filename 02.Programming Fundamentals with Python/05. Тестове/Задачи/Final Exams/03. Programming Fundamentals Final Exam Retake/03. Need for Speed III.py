# You have just bought the latest and greatest computer game – Need for Seed III. We know that you
# can`t wait to start playing. Pick your favorite cars and drive them all you want!
# On the first line of the standard input you will receive an integer n – the number of cars that you can obtain.
# On the next n lines the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
# {car}|{mileage}|{fuel}
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop"
# command is given:
# •	Drive : {car} : {distance} : {fuel}
# o	You need to drive the given distance and you will need the given fuel to do that. If the car doesn`t
# have enough fuel print:
# "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance,
# decrease its fuel with the given fuel and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if the mileage of a car reaches 100 000 km, remove it from the
# collection(s). Print:
# "Time to sell the {car}!"
# •	Refuel : {car} : {fuel}
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can
# fit in the tank, take only what is required to fill it up.
# o	Print a message in the following format:
# "{car} refueled with {fuel} liters"
# •	Revert : {car} : {kilometers}
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased
# it with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command you need to print all cars in your possession, sorted by their mileage
# in descending order, then by their name in ascending order, in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
# •	The mileage and fuel of the cars will be valid, 32-bit integers and will never be negative.
# •	The fuel and distance amounts in the commands will never be negative.
# •	The car names in the commands will always be valid cars in your possession.
our_dict = {}
n = int(input())
for b in range(n):
	c, m, f = input().split("|")
	our_dict[c] = [int(m), int(f)]

command = input()
while command != 'Stop':
	command = command.split(" : ")
	if len(command) == 4:
		_, car, distance, fuel = command
		if int(fuel) > our_dict[car][1]:
			print('Not enough fuel to make that ride')
		else:
			our_dict[car] = [our_dict[car][0] + int(distance), our_dict[car][1] - int(fuel)]
			print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
			if our_dict[car][0] >= 100000:
				print(f'Time to sell the {car}!')
				our_dict.pop(car)
	else:
		c, car, fuel_or_kilometer = command
		if c == 'Refuel':
			f = int(fuel_or_kilometer)
			if f + our_dict[car][1] > 75:
				fill = 75 - our_dict[car][1]
				our_dict[car][1] = 75
			else:
				fill = f
				our_dict[car][1] += fill
			print(f"{car} refueled with {fill} liters" )
		elif c == 'Revert':
			kilometers = int(fuel_or_kilometer)
			if our_dict[car][0] > 10000:
				if our_dict[car][0] - kilometers < 10000:
					our_dict[car][0] = 10000

				else:
					print(f"{car} mileage decreased by {kilometers} kilometers")
					our_dict[car][0] -= kilometers
			else:
				our_dict[car][0] -= kilometers
				print(f"{car} mileage decreased by {kilometers} kilometers")
	command = input()

for key, value in sorted(our_dict.items(), key=lambda x: (-x[1][0], x[0])):
	print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')


