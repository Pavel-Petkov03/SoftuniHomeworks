#  Това е 10 задача от урок 1 - Упражнения
# Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
# като имате предвид следната таблица:
# Градуси	Време
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold
# Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".

degrees = float(input())

if degrees >= 26.00 and degrees < 35.00:
    print("Hot")
elif degrees >= 20.1 and degrees <= 25.9:
    print("Warm")
elif degrees >= 15.00 and degrees <= 20.00:
    print("Mild")
elif degrees >= 12.00 and degrees <= 14.9:
    print("Cool")
elif degrees >= 5.00 and degrees <= 11.9:
    print("Cold")
else:
    print("unknown")
