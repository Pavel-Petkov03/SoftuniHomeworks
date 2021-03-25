# Write a function called operate that receives an operator(+, -, * or /) as first argument and multiple numbers as
# additional arguments (*args). The function should return the
# result of the operator applied to all the numbers. For more
# clarification, see the examples below. Submit only the function in the judge system.
def get_info(**kwargs):
	return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
