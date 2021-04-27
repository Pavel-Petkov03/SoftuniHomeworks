def reverse_text(text):
    start = len(text) - 1
    while start >= 0:
        yield text[start]
        start -= 1

for char in reverse_text("step"):
    print(char, end='')

