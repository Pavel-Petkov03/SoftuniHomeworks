# Our favorite super-spy action hero Sam is back from his mission in the previous exam, and he has
# finally found some time to go on a holiday. He is taking his wife somewhere nice and they're going
# to have a really good time, but first, they have to get there. Even on his holiday trip, Sam is still
# going to run into some problems and the first one is, of course, getting to the airport. Right now, he
# is stuck in a traffic jam at a very active crossroads where a lot of accidents happen.
# Your job is to keep track of traffic at the crossroads and report whether a crash happened or everyone
# passed the crossroads safely and our hero is one step closer to a much desired vacation.
# The road Sam is on has a single lane where cars queue up until the light goes green. When it does, they
# start passing one by one during the green light and the free window before the intersecting road's light
# goes green. During one second only one part of a car (a single character) passes the crossroads. If a car
# is still in the crossroads when the free window ends, it will get hit at the first character that is still
# in the crossroads.
# Input
# •	On the first line, you will receive the duration of the green light in seconds – an integer in the range [1-100]
# •	On the second line, you will receive the duration of the free window in seconds – an integer in the range [0-100]
# •	On the following lines, until you receive the "END" command, you will receive one of two things:
# 	A car – a string containing the model of the car, or
# 	The command "green" which indicates the start of a green light cycle
# A green light cycle goes as follows:
# •	During the green light cars will enter and exit the crossroads one by one
# •	During the free window cars will only exit the crossroads
# Output
# •	If a crash happens, end the program and print:
# "A crash happened!"
# "{car} was hit at {character_hit}."
# •	If everything goes smoothly and you receive an "END" command, print:
# "Everyone is safe."
# "{total_cars_passed} total cars passed the crossroads."


from collections import deque
green_time = int(input())
window_time = int(input())
command = input()
my_deque = deque()
is_break = False
car = None
passed = 0
while command != 'END':
	if command != 'green':
		my_deque.append(command)
	else:
		if my_deque:
			initial_car = my_deque.popleft()
			car = deque([c for c in initial_car])
			passed += 1
			for times in range(green_time):
				if car:
					car.popleft()
				else:
					if my_deque:
						initial_car = my_deque.popleft()
						car = deque([c for c in initial_car[1:]])
						passed += 1
					else:
						break
			if window_time < len(car):
				print('A crash happened!')
				print(f'{initial_car} was hit at {car[window_time]}.')
				is_break = True
				break
	command = input()
if not is_break:
	print(f'Everyone is safe.')
	print(f'{passed} total cars passed the crossroads.')
