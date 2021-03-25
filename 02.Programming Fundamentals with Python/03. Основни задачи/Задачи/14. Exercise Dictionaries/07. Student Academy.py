# Write a program that keeps information about students and their grades.
# You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade.
# Check if the student already exists and if not, add him. Keep track of all grades for each student.
# When you finish reading the data, keep the students with average grade higher than or equal to 4.50. Order the
# filtered students by average grade in descending order.
# Print the students and their average grade in the following format:
# {name} –> {averageGrade}
# Format the average grade to the 2nd decimal place.
name_count = {}
final_dict = {}
n = int(input())
for times in range(0 , n):
	name = input()
	grade = float(input())
	if name in final_dict:
		name_count[name].append(grade)
		final_dict[name] = sum(name_count[name]) / len(name_count[name])
	else:
		final_dict[name] = grade
		name_count[name] = [grade]

new_dict = {key: value for key, value in final_dict.items() if value >= 4.5}
for name, score in sorted(new_dict.items(), key=lambda x: -x[1]):
	print(f'{name} -> {score:.2f}')


