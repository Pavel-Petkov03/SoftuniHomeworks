# Every day thousands of people pass by the reception at "National Court" with various questions to ask and the
# employees have to help everyone by providing correct information and to answer all questions.
# There are 3 employees working on the reception all day long. Each of them can handle different number of people per
# hour. Your task is to calculate how much time it will take to answer all the questions of a given number of people.
# First you will receive 3 lines with integers, representing the count of people that each of the employee can help
# per hour. On the next line you will receive the total people count as a single integer.
# Every fourth hour all the employees have a one-hour break before they start working again. This is the only break
# they get because they don`t need rest and have no personal life. Calculate the time needed to answer all people`s
# questions and print it in the following format: "Time needed: {time}h."
# Input / Constraints
# •	On first three lines -  each employee`s efficiency -  an integer in the range [1 - 100]
# •	On the fourth line - people count – an integer in the range [0 – 10000]
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


