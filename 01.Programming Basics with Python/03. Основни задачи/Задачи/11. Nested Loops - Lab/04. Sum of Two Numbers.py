# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа. На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]
# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# •	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# •	Ако не е намерена комбинация отговаряща на условието
# o	"{броят на всички комбинации} combinations - neither equals {магическото число}"
start = int(input())
end = int(input())
magical_number = int(input())
number_of_iterations = 0
is_found = False
first_number = 0
second_number = 0
for first_number in range(start , end + 1):
    for second_number in range(start , end + 1):
        number_of_iterations += 1
        if first_number + second_number == magical_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{number_of_iterations} ({first_number} + {second_number} = {magical_number})")
else:
    print(f"{number_of_iterations} combinations - neither equals {magical_number}")