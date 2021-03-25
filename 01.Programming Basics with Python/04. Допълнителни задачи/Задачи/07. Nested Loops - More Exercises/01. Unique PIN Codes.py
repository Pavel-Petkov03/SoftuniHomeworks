#  1.	Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал. За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# •	Първата и третата цифра трябва да бъдат четни.
# •	Втората цифра трябва да бъде просто число в диапазона [2...7].
# Вход
# От конзолата се четат 3 реда:
# •	Горната граница на първото число - цяло число в диапазона [1...9]
# •	Горната граница на второто число - цяло число в диапазона [1...9]
# •	Горната граница на третото число - цяло число в диапазона [1...9]
# Изход
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали.
max_for_first = int(input())
max_for_second = int(input())
max_for_third = int(input())
is_prime = False
for first in range(2 , max_for_first + 1):
    if first % 2 == 0:
        for second in range( 2, max_for_second + 1 ):
            for i in range( 2,second):
                if second % i == 0:
                    break
            else:
                for third in range( 2, max_for_third + 1 ):
                    if third % 2 == 0:
                        print(f'{first} { second} {third}')
















