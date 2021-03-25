
def adding(dict_, name_, course_, points_):
	if name not in dict_:
		dict_[name_] = {course_: points_}
	else:
		if course in dict_[name_]:
			if int(dict_[name_][course_]) <= int(points_):
				dict_[name_][course_] = points_
		else:
			dict_[name_].update({course_: points_})
	return dict_


def banned(dict_, name_):
	if name in dict_:
		dict_.pop(name_)
	return dict_


def counting(dict_, course_):
	if course_ not in dict_:
		dict_[course_] = 1
	else:
		dict_[course_] += 1
	return dict_


our_dict = {}
counting_dict = {}
command = input()
while command != "exam finished":
	command = command.split("-")
	if len(command) == 2:
		name, _ = command
		our_dict = banned(our_dict, name)
	else:
		name, course, points = command
		our_dict = adding(our_dict, name, course, points)
		counting_dict = counting(counting_dict, course)
	command = input()
new_dict = {}
print('Results:')
for name, course_and_points in our_dict.items():
	for course, points in course_and_points.items():
		new_dict.update({name: points})
for username, points in sorted(new_dict.items(), key=lambda x: (-int(x[1]), x[0])):
	print(f'{username} | {points}')
print('Submissions:')
for language, count in sorted(counting_dict.items(), key=lambda x: (-x[1], x[0])):
	print(f'{language} - {count}')
