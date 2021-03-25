# Kate is stuck into a maze, you have to help her to find her way out
# On the first line you will be given how many rows there are in the maze. On the next n
# lines you will be given the maze itself. Here is a legend for the maze:
# •	"#" - means a wall; Kate cannot go through there
# •	" " - means empty space; Kate can go through there
# •	"k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not. If Kate can get out print the following:
# "Kate got out in {number_of_moves} moves". Otherwise print: "Kate cannot get out"


maze = []
for row in range(int(input())):
	maze.append([c for c in input()])
k_pos = ''
for row in range(len(maze)):
	is_break = False
	for col in range(len(maze[row])):
		if maze[row][col] == 'k':
			k_pos = [row , col]
			is_break = True
			break
	if is_break:
		break
def kate(maze_ , pos , t):
	row_ = int(pos[0])
	col_ = int(pos[1])
	if row_ != len(maze) -1 and col_ != len(maze[row_]) - 1:
		if col_ + 1 in range(len(maze[row_])) and maze[row_][col_+1] == ' ':
			maze[row_][col_+1] = '#'
			col_ += 1
		elif row_ + 1 in range(len(maze)) and maze[row_+1][col_] == ' ':
			maze[row_+1][col_] = '#'
			row_ += 1
		elif col_ - 1 in range(len(maze[row_])) and maze[row_][col_-1] == ' ':
			maze[row_][col_-1] = '#'
			col_ -= 1
		elif row_ - 1 in range(len(maze)) and maze[row_-1][col_] == ' ':
			maze[row_-1][col_] = '#'
			row_ -= 1
		elif row_ == 0 or col_ == 0 or row_ == len(maze_) - 1 or col_ == len(maze[0]):
			return f'Kate got out in 1 moves'
		else:
			return 'Kate cannot get out'
		t += 1
		return kate(maze_, [row_, col_], t)
	t += 1
	return f'Kate got out in {t} moves'



print(kate(maze, k_pos, 0))




