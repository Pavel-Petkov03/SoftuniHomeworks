# Трябва да се пресметне обемът на басейн под формата на паралелепипед ако знаем неговата дължина, широчина и дължина:
# В басейна има част която е заета от помпа(Тя се кварва в конзолата в проценти)
# Конзолата трябва да отпечата останалото място в басейна:
length = int(input())
width = int(input())
height = int(input())
taken_place_percent = float(input()) * 0.01
available_place = (length * width * height * 0.001) - taken_place_percent * (length * width * height * 0.001)
print(available_place)
