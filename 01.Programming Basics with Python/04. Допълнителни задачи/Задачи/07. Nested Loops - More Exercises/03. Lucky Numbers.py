# Да се напише програма, която прочита едно цяло число N и генерира всички възможни "щастливи" и различни 4-цифрени числа(всяка цифра от числото е в интервала [1...9]).
# Числото трябва да отговаря на следните условия:
# Щастливо число е 4-цифрено число, на което сбора от първите две цифри е равен на сбора от последните две. Числото N трябва да се дели без остатък от сбора на първите две цифри на "щастливото" число.
# Вход
# Входът се чете от конзолата и се състои от едно цяло число в интервала [2...10000]
# Изход
# На конзолата трябва да се отпечатат всички "щастливи" и различни 4-цифрени числа, разделени с интервал
number = int(input())
first_two_letters = 0
second_two_letters = 0
compiler = 0
is_time = False
for car_number in range(1000 , 10000):
    symbol = str(car_number)
    first_two_letters = 0
    second_two_letters = 0
    compiler = 0
    for index , digit in enumerate(symbol):
        digit = int(digit)
        if digit != 0:
            if index <= 1:
                first_two_letters += digit
                compiler += 1
            else:
                second_two_letters += digit
                compiler += 1
            if first_two_letters == 0 and compiler == 4:
                break
            else:
                if number % first_two_letters == 0 and first_two_letters == second_two_letters and compiler == 4 :
                    print(symbol , end =' ')











