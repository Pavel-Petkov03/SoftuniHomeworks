import re

final_list = []
all_calories = 0
pattern = r'([#\|])(?P<item_name>[A-Za-z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,})\1'
for match in re.finditer(pattern, input()):
    dict_representation = match.groupdict()
    final_list.append(dict_representation)
    all_calories += int(dict_representation['calories'])

print(f'You have food to last you for: {all_calories // 2000} days!')
for my_dict in final_list:
    print(f'Item: {my_dict["item_name"]}, Best before: {my_dict["expiration_date"]}, Nutrition: {my_dict["calories"]}')
