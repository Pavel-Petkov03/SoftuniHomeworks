# Write a function that checks if a given password is valid. Password validations are:
# •	The length should be 6 - 10 characters (inclusive)
# •	It should consists only letters and digits
# •	It should have at least 2 digits
# If a password is valid print "Password is valid".
# If it is NOT valid, for every unfulfilled rule print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"
def password_generator(text):
    is_ok = True
    num_count = 0
    all_count = 0
    actual_result = ''
    is_not_only_numbers_and_digits = False
    for index in range(len(text)):
        if 48 <= ord(text[index]) <= 57:
            num_count += 1
        elif 65 <= ord(text[index]) <= 97 or 65 <= ord(text[index]) <= 122:
            pass
        else:
            is_not_only_numbers_and_digits = True
        all_count += 1

    if all_count < 6 or all_count > 10:
        actual_result += "Password must be between 6 and 10 characters\n"
        is_ok = False
    if is_not_only_numbers_and_digits:
        actual_result += "Password must consist only of letters and digits\n"
        is_ok = False
    if num_count < 2:
        actual_result += "Password must have at least 2 digits\n"
        is_ok = False
    if is_ok:
        actual_result += "Password is valid"
    return  actual_result


actual_text = input()
print(password_generator(actual_text))
