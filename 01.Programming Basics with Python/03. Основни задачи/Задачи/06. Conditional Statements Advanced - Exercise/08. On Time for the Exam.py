# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# Първият ред съдържа час на изпита – цяло число от 0 до 23;
# Вторият ред съдържа минута на изпита – цяло число от 0 до 59;
# Третият ред съдържа час на пристигане – цяло число от 0 до 23;
# Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
# "Late", ако студентът пристига по-късно от часа на изпита;
# "On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# "Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# "mm minutes before the start" за идване по-рано с по-малко от час;
# "hh:mm hours before the start" за подраняване с 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:05”;
# "mm minutes after the start" за закъснение под час;
# "hh:mm hours after the start" за закъснение от 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:03”.
real_h = int(input())
real_m = int(input())
arrival_h = int(input())
arrival_m = int(input())
real_time = real_h * 60 + real_m
arrival_time = arrival_h * 60 + arrival_m
difference = abs(real_time - arrival_time)
rounded_hour = abs(real_time - arrival_time)//60
rounded_minute = abs(real_time - arrival_time)% 60
if arrival_time > real_time:
    print("Late")
elif arrival_time >= real_time - 30 :
    print("On time")
elif arrival_time < real_time:
    print("Early")
if real_time >= arrival_time:
    if difference < 60:
        print(f'{rounded_minute} minutes before the start')
    elif difference >= 60:
        if rounded_minute < 10:
            print(f'{rounded_hour}:0{rounded_minute} hours before the start')
        elif rounded_minute > 10:
            print(f'{rounded_hour}:{rounded_minute} hours before the start')
elif arrival_time > real_time:
    if difference < 60:
        print(f'{rounded_minute} minutes after the start')
    elif difference >= 60:
        if rounded_minute < 10:
            print(f'{rounded_hour}:0{rounded_minute} hours after the start')
        elif rounded_minute > 10:
            print(f'{rounded_hour}:{rounded_minute} hours after the start')




