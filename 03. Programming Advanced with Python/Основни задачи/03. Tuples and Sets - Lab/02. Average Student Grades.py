# Write a program, which reads a name of a student and their grades and adds them to the student record.
# Print the name of the students with their grades and their average grade.
# The order in which we print the result does not matter.


n = int(input())
average_dict = {}
for c in range(n):
	name, grade = input().split()
	grade = float(grade)
	if name not in average_dict:
		average_dict[name] = []
	average_dict[name].append(grade)

for key, value in average_dict.items():
	join_grades = [f'{grade:.2f}' for grade in value]
	print(f'{key} -> {" ".join(join_grades)} (avg: {(sum(value) / len(value)):.2f})')