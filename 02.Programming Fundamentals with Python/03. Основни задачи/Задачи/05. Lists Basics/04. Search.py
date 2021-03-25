# You will receive a number n and a word. On the next n lines you will be given some strings. You have to add them in a
# list and print them. After that you have to filter
# out only the strings that include the given word and print that list too.
n =int(input())
wanted_word = input()
all_list = []
exclusive_list = []
for c in range(1 , n +1):
    quote = input()
    all_list.append(quote)
    if quote.count(wanted_word) != 0:
        exclusive_list.append(quote)
print(all_list)
print(exclusive_list)
