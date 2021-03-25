# You Will Receive Two Lines of Input: a List of Employee's
# Happiness As String with Numbers Separated by a Single Space
# and a Happiness Improvement Factor (Single Number).
# Your Task is to Find Out If the Employees Are Generally
# Happy in Their Office. To Do That You Have to Increase
# Happiness by Multiplying the All the Employee's Happiness
# (the Numbers from the List) by the Factor, Filter the Employees
# Which Happiness is Greater Than or Equal to the Average in the New List and Print the Result
# There are two types of output:
# •	If the half or more of the employees have happiness >=
# than the average: "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise: "Score: {happy_count}/{total_count}. Employees are not happy!"
def happy(array , multiplyer):
	new_list = list(map(lambda x: int(x) * int(multiplyer) , array.split()))
	filtered = list(filter(lambda x: x >= sum(new_list) / len(new_list) , new_list))
	if len(filtered) >= len(new_list) / 2:
		return f'Score: {len(filtered)}/{len(new_list)}. Employees are happy!'
	else:
		return f"Score: {len(filtered)}/{len(new_list)}. Employees are not happy!"

our_array = input()
our_mul = input()
print(happy(our_array,our_mul))






