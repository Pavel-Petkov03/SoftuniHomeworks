# Write a program that keeps information about companies and their employees.
# You will be receiving a company name and an employee's id, until you receive the command "End" command. Add each
# employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# When you finish reading the data, order the companies by the name in ascending order.
# Print the company name and each employee's id in the following format:
# {companyName}
# -- {id1}
# -- {id2}
# -- {idN}
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
# •	The input always will be valid.
our_dict = {}
command = input()
while command != "End":
	name, idi = command.split(" -> ")
	if name in our_dict:
		if idi not in our_dict[name]:
			our_dict[name].append(idi)
	else:
		our_dict[name] = [idi]
	command = input()

for key, _ in sorted(our_dict.items() , key = lambda x : x[0]):
	print(key)
	for idi in our_dict[key]:
		print(f'-- {idi}')

