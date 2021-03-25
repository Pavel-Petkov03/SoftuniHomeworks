# You are at the shooting gallery again and you need a program that helps you keep track of moving targets.
# On the first line, you will receive a sequence of targets with their integer values, split by a single space.
# Then, you will start receiving commands for manipulating the targets, until the "End" command. The commands are
# the following:
# •	Shoot {index} {power}
# o	Shoot the target at the index, if it exists by reducing its value by the given power (integer value).A target
# is considered shot when its value reaches 0.
# o	Remove the target, if it is shot.
# •	Add {index} {value}
# o	Insert a target with the received value at the received index, if it exist. If not, print: "Invalid placement!"
# •	Strike {index} {radius}
# o	Remove the target at the given index and the ones before and after it depending on the radius, if such exist.
# If any of the indices in the range is invalid print:
# "Strike missed!" and skip this command.
#  Example:  Strike 2 2
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# •	End
# o	Print the sequence with targets in the following format:
# {target1}|{target2}…|{targetn}
# Input / Constraints
# •	On the first line you will receive the sequence of targets – integer values [1-10000].
# •	On the next lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when "Strike" command would empty the whole sequence.
# Output
# •	Print the appropriate message in case of "Strike" command if necessary.
# •	In the end, print the sequence of targets in the format described above.

array = [{c:j} for c , j in enumerate(input())]

command = input()
while command != 'End':
	task, index, doing = command.split()
	doing = int(doing)
	index = int(index)
	if task == 'Shoot':
		if 0 <= index <= len(array) - 1:
			array[index] -= doing
			if array[index] <= 0:
				array.pop(index)
	elif task == 'Add':
		if 0 <= index <= len(array) - 1:
			array.insert(index, doing)
		else:
			print('Invalid placement!')
	elif task == 'Strike':
		if index + doing in range(len(array)) and index - doing in range(len(array)):
			new_array = []
			for i in range(0, index - doing):
				new_array.append(array[i])
			for i in range(index + doing + 1, len(array)):
				new_array.append(array[i])
			array = new_array.copy()
			new_array.clear()
		else:
			print("Strike missed!")
	command = input()

print('|'.join([str(c) for c in array]))
print(array)
