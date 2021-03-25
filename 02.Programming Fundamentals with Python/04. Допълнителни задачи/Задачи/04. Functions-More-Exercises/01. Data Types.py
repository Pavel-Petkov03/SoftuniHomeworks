# Write a program that, depending on the first line of the input, reads an int, double or string.
# •	If the data type is int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.
# •	If the data type is string, surround the input with "$".
# Print the result on the console.
def types_(type_ , text):
    if type_ == "string":
        return f'${text}$'
    elif type_ == "int":
        return 2 * int(text)
    elif type_ == "real":
        return f"{(1.5 * float(text)):.2f}"


our_type = input()
our_text = input()
print(types_(our_type , our_text))



