# Write a program that keeps information about courses.
# Each course has a name and registered students.
# You will be receiving a course name and a student name, until you receive the command "end".
# Check if such course already exists, and if not, add the course. Register the user into the course.
# When you receive the command "end", print the courses with their names and total registered users,
# ordered by the count of registered users in descending order. For each contest print the registered
# users ordered by name in ascending order.
# Input
# �	Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".
# �	The product data is always delimited by " : ".
# Output
# �	Print the information about each course in the following the format:
# "{courseName}: {registeredStudents}"
# �	Print the information about each student, in the following the format:
# "-- {studentName}"
iterable_dict = {}
person_dict = {}
command = input()
while command != "end":
	course, name = command.split(" : ")
	if course in iterable_dict:
		iterable_dict[course] += 1
		person_dict[course].append(name)
	else:
		iterable_dict[course] = 1
		person_dict[course] = [name]
	command = input()

for key, value in sorted(iterable_dict.items(), key=lambda x: -x[1]):
	print(f'{key}: {value}')
	for students in sorted(range(len(person_dict[key])), key=lambda x: person_dict[key][x]):
		print(f"-- {person_dict[key][students]}")




