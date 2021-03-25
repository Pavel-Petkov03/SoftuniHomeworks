# Напишете програма, която първоначално прочита име и парола на потребителски профил.
# След това чете парола за вход, при въвеждане на грешна парола,
# потребителя да се подкани да въведе нова парола.
username = input()
actual_password = input()
password = input()
while password != actual_password:
    password = input()
else:
    print(f"Welcome {username}!")
