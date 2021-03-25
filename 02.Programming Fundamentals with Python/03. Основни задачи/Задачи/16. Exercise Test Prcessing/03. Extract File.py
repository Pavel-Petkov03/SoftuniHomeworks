# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input().split('\\')
wanted_place = path[-1]
file , extension = wanted_place.split(".")
print(f'File name: {file}')
print(f'File extension: {extension}')
