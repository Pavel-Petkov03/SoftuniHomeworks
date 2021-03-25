# Calculate how many courses will be needed to elevate n persons by using an elevator with
# capacity of p persons. The input holds two lines: the number of people n and the capacity p of the elevator.
people = int(input())
capacity = int(input())
times = 0
while True:
    if capacity >= people:
        times += 1
        break
    people -= capacity
    times += 1
print(times)
