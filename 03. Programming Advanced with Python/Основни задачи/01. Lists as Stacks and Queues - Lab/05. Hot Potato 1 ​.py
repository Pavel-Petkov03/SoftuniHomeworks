# Hot potato is a game in which children form a circle and start passing a hot potato. The counting starts with the
# 	first kid. Every nth toss the child left with the potato leaves the game. When a kid leaves the game, it passes
# 	the potato along. This continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. Print every kid that is removed from the circle. In the end,
# print the kid that is left last.

from collections import deque
my_deque = deque([c for c in input().split()])
step = int(input())
counter = 1
while len(my_deque) > 1:
	if counter == step:
		print(f'Removed {my_deque.popleft()}')
		counter = 0
	else:
		my_deque.append(my_deque.popleft())

	counter += 1

print(f'Last is {my_deque.popleft()}')


