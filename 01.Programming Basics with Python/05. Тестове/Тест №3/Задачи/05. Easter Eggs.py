import sys
# Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца. Наличните цветове за боядисване са:
# •	червено (red)
# •	оранжев (orange)
# •	син (blue)
# •	зелен (green)
# Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят
# и от кой цвят яйцата са най - много, като знаете общия им брой и цвета
# на всяко яйце.
# Вход
# От конзолата се чете 1 ред:
# •	 Броят на боядисаните яйца – цяло число в интервала [1 ... 100]
# За всяко яйце се чете:
# o	Цветът на яйцето – текст с възможности: "red", "orange", "blue", "green"
# Изход
# Да се отпечатат на конзолата 5 реда:
# •	"Red eggs: {брой на червените яйца}"
# •	"Orange eggs: {брой на оранжевите яйца}"
# •	"Blue eggs: {брой на сините яйца}"
# •	"Green eggs: {брой на зелените яйца}"
# •	"Max eggs: {максимален брой на яйцата от цвят} -> {цвят}"
count = int(input())
red = 0
orange = 0
blue = 0
green = 0
color_name = ''
max = -sys.maxsize
for c in range(1 , count +1 ):
    color = input()
    if color == "red":
        red += 1
        if red > max:
            max = red
            color_name = "red"
    elif color == "orange":
        orange += 1
        if orange > max:
            max = orange
            color_name = "orange"
    elif color == "blue":
        blue += 1
        if blue > max:
            max = blue
            color_name = "blue"
    elif color == "green":
        green += 1
        if green > max:
            max = green
            color_name = "green"
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max} -> {color_name}")

