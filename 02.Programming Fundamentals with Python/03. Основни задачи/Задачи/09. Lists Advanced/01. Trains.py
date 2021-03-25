# You will receive how many wagons the train has. Create a list with that length with all zeros. Until you receive the command "End", you get some of the following commands:
# •	add {people} -> adds the people in the last wagon
# •	insert {index} {people} -> adds the people at the given wagon
# •	leave {index} {people} -> removes the people from the wagon
# After you receive the "End" command print the train

def array_manipulation(times):
    array = [0 for _ in range(times)]
    command = input()
    while command != "End":
        command.split()
        if command.split()[0] == "add":
            array[-1] += int(command.split()[1])
        elif command.split()[0] == "insert":
            number = array[int(command.split()[1])] + int(command.split()[2])
            array.pop(int(command.split()[1]))
            array.insert(int(command.split()[1]), number )
        elif command.split()[0] == "leave":
            number = array[int(command.split()[1])] - int(command.split()[2])
            array[int(command.split()[1])] = number
        command = input()
    return array


our_times = int(input())
print(array_manipulation(our_times))
