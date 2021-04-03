import re
pattern = r"^(.+)>(?P<digits>\d+)\|(?P<lower_case>([a-z]+))\|(?P<upper_case>([A-Z])+)\|(?P<symbols>([^<>]\S+[^<>]))<\1$"
for _ in range(int(input())):
    word = input()
    is_match = False
    for m in re.finditer(pattern, word):
        is_match = True
        dect = m.groupdict()
        print(f'Password: {dect["digits"]}{dect["lower_case"]}{dect["upper_case"]}{dect["symbols"]}')

    if not is_match:
        print('Try another password!')


