# Create a function called age_assignment that receives different number of names and then different number of
# key-value pairs. The key will be a single letter
# (first letter of a name), and the value a
# number (age). For each name, find its first
# letter in the key-value pairs and assign the age to the
# person's name. At the end return a dictionary with all the names and ages as shown in the ' \
# 	  'example. Submit only the function in the judge system.


def age_assignment(*args, **kwargs):
    final_dict = {}
    for item in args:
        if item[0] in kwargs:
            final_dict[item] = kwargs[item[0]]

    return final_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

