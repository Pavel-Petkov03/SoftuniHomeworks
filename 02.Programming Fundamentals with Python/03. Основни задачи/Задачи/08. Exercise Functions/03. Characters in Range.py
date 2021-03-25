# Write a function that receives two characters and returns a single string with all the characters in
# between them according to the ASCII code.
def m(s, e):
    result = ''
    for c in range(ord(s) + 1, ord(e)):
        result += f'{chr(c)} '
    return result


start = input()
end = input()
print(m(start, end))
