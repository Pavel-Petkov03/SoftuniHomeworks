# Write a program that finds the longest intersection. You will be given a number N.
# On the next N lines you will be given two ranges in the format: "{first_start},
# {first_end}-{second_start},{second_end}". Find the intersection of these two ranges and save the longest one of all
# N intersections. At the end print the numbers that are included in the longest intersection and its length in the
# format: "Longest intersection is {longest_intersection} with length {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.


max_len_set = set()
for _ in range(int(input())):
	first_intersection, second_intersection = input().split('-')
	first_in_first, second_in_first = first_intersection.split(',')
	first_in_second, second_in_second = second_intersection.split(',')
	a = {c for c in range(int(first_in_first), int(second_in_first) + 1)}.intersection({d for d in range(int(first_in_second), int(second_in_second) + 1)})
	if len(a) > len(max_len_set):
		max_len_set = a
print(f'Longest intersection is [{", ".join(map(str ,max_len_set))}] with length {len(max_len_set)}')
