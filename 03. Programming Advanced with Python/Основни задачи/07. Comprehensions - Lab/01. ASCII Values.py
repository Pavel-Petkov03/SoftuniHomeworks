# Write program that receives a list of characters and creates a dictionary with each character as a key and its
# ASCII value as a value. Try solving that problem using comprehensions.

print({c:ord(c) for c in input().split(', ')})