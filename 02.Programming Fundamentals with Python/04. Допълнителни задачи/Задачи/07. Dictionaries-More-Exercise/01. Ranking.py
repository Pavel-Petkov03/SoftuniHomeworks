# Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
# The final ranking is determined by the points of the interview tasks and from the exams in SoftUni.
# Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}"
# until you receive "end of contests". Save that data because you will need it later.
# After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you
# receive "end of submissions". Here is what you need to do.
# •	Check if the contest is valid (if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	Save the user with the contest they take part in (a user can take part in many contests) and the points the user
# has in the given contest. If you receive the same contest and the same user update the points only if the new ones
# are more than the older ones.
# At the end you have to print the info for the user with the most points in the format "Best candidate is {user} with
# total {total points} points.". After that print all students ordered by their names. For each user print each contest
# with the points in descending order. See the examples.
# Input
# •	strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case
# with two equal contests
# •	strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with same total points!
# Output
# •	On the first line print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# {user1 name}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# Constraints
# •	the strings may contain any ASCII character except from (:, =, >)
# •	the numbers will be in range [0 - 10000]
# •	second input is always valid
def add_(dict_, course_, password_, name_, points_):
	if name_ not in dict_:
		if course_ in template_dict:
			if template_dict[course_] == password_:
				dict_[name_] = {course_: points_}
	else:
		if course_ in template_dict:
			if template_dict[course_] == password_:
				if name_ in dict_ and course_ in dict_[name_]:
					if int(dict_[name_][course_]) < int(points_):
						dict_[name_][course_] = points_
				else:
					dict_[name_][course_] = points_
	return dict_


template_dict = {}
command = input()
needed_dict = {}
while command != "end of contests":
	contest, password = command.split(":")
	if contest not in template_dict:
		template_dict[contest] = password
	command = input()

command = input()
while command != "end of submissions":
	contest, password, username, points = command.split("=>")
	if contest in template_dict:
		if template_dict[contest] == password:
			needed_dict = add_(needed_dict, contest, password, username, points)
	command = input()
max_ = 0
best_dict = {}
best_name = ''
best_points = 0
for name, course_points in needed_dict.items():
	p = 0
	for course, points in course_points.items():
		p += int(points)
	if p > max_:
		best_name = name
		best_points = p
		max_ = p

print(f'Best candidate is {best_name} with total {best_points} points.')
print('Ranking:')
for name, course_and_points in sorted(needed_dict.items(), key=lambda x: x[0]):
	print(name)
	for course, points in sorted(course_and_points.items(), key=lambda x: -int(x[1])):
		print(f'#  {course} -> {points}')
