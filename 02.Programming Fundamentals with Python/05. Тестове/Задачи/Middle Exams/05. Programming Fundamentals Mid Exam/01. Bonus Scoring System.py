max_bonus = 0
max_l = 0
count_students = int(input())
lectures = int(input())
additional_bonus = int(input())
for student in range(count_students):
	student_attendance = int(input())
	bonus = student_attendance / lectures * (5 + additional_bonus)
	if bonus > max_bonus:
		max_bonus = bonus
		max_l = student_attendance

if lectures == 0:
	print(f'Max Bonus: 0.')
	print(f'The student has attended 0 lectures.')
else:
	print(f'Max Bonus: {round( max_bonus )}.')
	print(f'The student has attended {max_l} lectures.')


