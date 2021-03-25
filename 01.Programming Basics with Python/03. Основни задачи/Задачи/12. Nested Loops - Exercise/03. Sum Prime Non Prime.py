# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"
sum_of_prime_number = 0
sum_of_non_prime_number = 0
command = input()
while command != 'stop':
    is_prime = True
    number = int(command)
    if number < 0:
        command = input()
        print('Number is negative.')
        continue
    for checking in range(2 , number):
        if number % checking == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        sum_of_prime_number += number
    else:
        sum_of_non_prime_number += number
    command = input()
print(f'Sum of all prime numbers is: {sum_of_prime_number}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime_number}')