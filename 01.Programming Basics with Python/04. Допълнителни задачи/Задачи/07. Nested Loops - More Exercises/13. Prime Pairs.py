# Напишете програма, която генерира и принтира на конзолата четирицифрени числа, в които първата и втората двойка цифри образуват двуцифрени прости числа (пример за такова число 1723). Крайната стойност до която трябва да се генерират двойките се определя от други 2 цифри, подадени като вход, които определят с колко крайната стойност е по-голяма от началната.
# Вход
# От конзолата се четат четири реда:
# •	На първия ред – началната стойност на първите първата двойка числа – цяло положително число в диапазона [10… 90]
# •	На втория ред – началната стойност на втората двойка числа – цяло положително число в диапазона [10… 90]
# •	На третия ред – разликата между началната и крайната стойност на  първата двойка числа – цяло положително число в диапазона [1… 9]
# •	На четвъртия ред – разликата между началната и крайната стойност на  втората двойка числа – цяло положително число в диапазона [1… 9]
# Изход:
# Да се отпечатат на конзолата четирицифрените числа, в които първите две и вторите две цифри са прости двуцифрени числа.
beginning_for_first_couple = int(input())
beginning_for_second_couple = int(input())
difference_for_first = int(input())
difference_for_second = int(input())
is_break = False
for first in range(1 , 10):
    if is_break:
        break
    for second in range( 1, 10 ):
        if is_break:
            break
        for third in range( 1, 10 ):
            if is_break:
                break
            for forth in range( 1, 10 ):
                if is_break:
                    break
                for first_couple in range(beginning_for_first_couple , beginning_for_first_couple + difference_for_first + 1):
                    for match in range(2 , first_couple):
                        is_break = True
                        if first_couple % match == 0:
                            break
                    else:
                        for second_couple in range(beginning_for_second_couple , beginning_for_second_couple + difference_for_second + 1):
                            for match in range(2 , second_couple):
                                if second_couple % match == 0:
                                    break
                            else:
                                print(f'{first_couple}{second_couple}')















