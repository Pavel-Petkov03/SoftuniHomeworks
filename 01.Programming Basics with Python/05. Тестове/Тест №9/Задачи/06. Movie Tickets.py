# Трябва да напишете програма, която чете три цели числа  a1, a2, n
# въведени от потребителя и генерира номера за билети, които се състоят от следните 4 символа:
# •	Символ 1: символ с ASCII код от а1 до а2 - 1
# •	Символ 2: цифра от 1 до n - 1
# •	Символ 3: цифра от 1 до n / 2 - 1
# •	Символ 4: цифрова репрезентация (ASCII код) на символ 1
# След като са изпълнени условията се генерира следния билет:
# "{Символ 1}-{Символ 2}{Символ 3}{Символ  4}"
# Вход
# •	a1 – цяло число в интервала [65… 89]
# •	a2 – цяло число в интервала [66… 91]
# •	n – цяло число в интервала [1… 10]
# Изход
# На конзолата трябва да се отпечатат всички билетни номера,
# на които числовата репрезентация на символ 1 е нечетна и сборът на символ 2,
# символ 3 и символ 4 е нечетен.
a1 = int(input())
a2 = int(input())
n = int(input())
for symbol1 in range(a1, a2):
    first = chr(symbol1)
    if symbol1 % 2 != 0:
        for second in range(1 , n):
            for third in range(1 , int((n/2))):
                forth = symbol1
                if (forth + second + third) % 2 != 0:
                    print(f"{first}-{second}{third}{forth}")


