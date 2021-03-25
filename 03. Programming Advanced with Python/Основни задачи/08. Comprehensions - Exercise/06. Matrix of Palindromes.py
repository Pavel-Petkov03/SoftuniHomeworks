# Write a program to generate the following matrix of palindromes of 3 letters with r
# rows and c columns like the one in the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter:
# o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …



initial_row, initial_col = list(map(int, input().split()))


def fill_matrix(m,r,c):
	for row in range(r):
		temp = []
		for col in range(c):
			temp.append(f'{chr( 97 + row )}{chr( 97 + row + col )}{chr( 97 + row )}' )
		m.append(temp.copy())
	return m


def print_result(m):
	return [print(' '.join(c)) for c in m]


matrix = fill_matrix([], initial_row, initial_col)
print_result(matrix)
