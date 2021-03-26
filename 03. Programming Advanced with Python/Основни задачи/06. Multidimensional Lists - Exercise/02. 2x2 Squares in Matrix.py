# Find the count of 2 x 2 squares of equal chars in a matrix.
# Input
# •	On the first line, you are given the integers rows and cols - the matrix's dimensions
# •	Matrix characters come at the next rows (space separated)
# Output
# •	Print the number of all the square matrices you have found

row, col = list(map(int, input().split()))
matrix = [input().split() for c in range(row)]
counter = 0


def check(row, col, mat):
	if mat[row][col] == mat[row+1][col] == mat[row][col+1] == mat[row+1][col+1]:
		return True
	return False


for row_ in range(row - 1):
	for col_ in range(col - 1):
		if check(row_, col_, matrix):
			counter += 1
print(counter)


