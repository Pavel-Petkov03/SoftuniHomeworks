# Това е пета задача от урок 1-Упражнения
# Трябва да се пресметне в зала колко места за маси и столове(в комплект) биха се събрали при зададени параметри на
# широчина и дължина на залата , за която знаем че е с правоъгълна форма и също , че
# Едно работно място заема 70 на 120 cm (маса с размер 70 на 40 cm + място за стол и преминаване с размер 70 на 80 cm).
# Коридорът е широк поне 100 cm. Изчислено е, че заради входната врата (която е с отвор 160 cm)
# се губи точно 1 работно място, а заради катедрата (която е с размер 160 на 120 cm) се губят точно 2 работни места.
length_of_hall = float(input()) * 100   # Широчина от метри в сантиметри
width_of_hall = float(input()) * 100 - 100  # Дължина от метри в сантиметри
row = length_of_hall // 120
place_per_row = width_of_hall // 70
places = place_per_row * row - 3
print(places)
