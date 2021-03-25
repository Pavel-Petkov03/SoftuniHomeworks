# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата,
# които гостите са взели преди тя да свърши. Ще получите размерите на тортата
# (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата "STOP"
# или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."
width = int(input())
length = int(input())
cake = width * length
command = input()
left_cake = False
taken_cake = 0
while command != "STOP":
    command = int(command)
    taken_cake += command
    if taken_cake > cake:
        left_cake = True
        break
    command = input()
if left_cake:
    print(f"No more cake left! You need {taken_cake - cake} pieces more.")
else:
    print(f"{cake - taken_cake} pieces are left.")


