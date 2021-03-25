# You are at the shooting gallery again and you need a program that helps
# you keep track of moving targets. On the first line, you will receive a sequence
# of targets with their integer values, split by a single space. Then, you will start
# receiving commands for manipulating the targets, until the "End" command. The commands are the following:
# •	Shoot {index} {power}
# o	Shoot the target at the index, if it exists by reducing its value by the given
# power (integer value).A target is considered shot when its value reaches 0.
# o	Remove the target, if it is shot.
# •	Add {index} {value}
# o	Insert a target with the received value at the received index, if it exist. If not, print: "Invalid placement!"
# •	Strike {index} {radius}
# o	Remove the target at the given index and the ones before and after it depending
# on the radius, if such exist. If any of the indices in the range is invalid print:
# "Strike missed!" and skip this command.
#  Example:  Strike 2 2
def manipulate_array(array):
	array = [int(array.split()[integer]) for integer in range(len(array.split()))]
	command = input()
	while command != "End":
		task , index , value = command.split()
		index , value = int(index) , int(value)
		if task == "Shoot":
			if index in range(0 , len(array)):
				array[index] -= value
				if array[index] <= 0:
					array.pop(index)
		elif task == "Add":
			if index in range( 0, len( array ) ):
				array.insert(index, value)
			else:
				print("Invalid placement!")
		elif task == "Strike":
			right_index = index + value
			left_index = index - value
			if right_index < len(array) and left_index >= 0:
				left_part = array[:left_index]
				right_part = array[right_index + 1:]
				array = left_part + right_part

			else:
				print("Strike missed!" )
		command = input()
	array = [str(array[stringed]) for stringed in range(len(array))]
	return "|".join(array)

our_array = input()
print(manipulate_array(our_array))


