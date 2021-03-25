# Every day thousands of students pass by the reception at SoftUni with different questions to ask and the employees
# have to help everyone by providing all the information and to answer all of the questions.
# There are 3 employees working on the reception all day. Each of them can handle different number of students per
# hour. Your task is to calculate how much time it will take to answer all the questions of given number of students.
# First you will receive 3 lines with integers, representing count of students that each of the employee can help per
# hour. On the next line you will receive students count as a single integer.
# Every forth hour all of the employees have a break, so they don’t work for a hour. This is the only break for the
# employees, because they don`t need rest, nor have a personal life. Calculate the time needed to answer all the
# student's questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# •	On first three lines -  each employee efficiency -  integer in range [1 - 100]
# •	On the fourth line - students count – integer in range [0 – 10000]
# •	Input will always be valid and in the range specified
# Output
# •	Print a single line: "Time needed: {time}h."
# •	Allowed working time / memory: 100ms / 16MB



needed_hours = 0
total_employees_efficiency = int( input() ) + int( input() ) + int( input() )
total_people_count = int(input())
while total_people_count > 0:
	total_people_count -= total_employees_efficiency
	needed_hours += 1
	if needed_hours % 4 == 0:
		needed_hours += 1

print(f"Time needed: {needed_hours}h.")


