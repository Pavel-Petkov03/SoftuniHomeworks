# Изпит по "Основи на програмирането" – 28 и 29 март 2020
# Задача 4. Храна за домашни любимци
# Ани има два домашни любимеца - куче и котка.
# Напишете програма, която изготвя статистика за храната на домашните любимци
# за определен брой дни. Всеки ден кучето и котката изяждат различно количество
# от общата им храна. На всеки трети ден получават награда - бисквитки.
# Количеството на бисквитките е 10% от общо изядената храна за деня.
# Вашата програма трябва да отпечатва статистика за количеството бисквитки,
# които са изяли, колко процента от първоначалното количество обща храна
# са изяли и колко процента от изядената храна е изяло кучето и колко е изяла
# котката.
# Вход
# Първоначално се чете един ред:
# •	Брой дни – цяло число в диапазона [1…30]
# •	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# o	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# o	Количество изядена храна от котката – цяло число в диапазона [10…500]
# Изход
# На конзолата да се отпечатват четири реда:
# •	"Total eaten biscuits: {количество изядени бисквитки}gr."
# •	"{процент изядена храна}% of the food has been eaten."
# •	"{процент изядена храна от кучето}% eaten from the dog."
# •	"{процент изядена храна от котката}% eaten from the cat."
# Количеството изядени бисквитки трябва да бъде закръглено до най –
# близкото цяло число, а процентът храна трябва да бъде форматиран до втората цифра след десетичния знак.
days = int(input())
all_food = float(input())
food_eaten_by_cat = 0
food_eaten_by_dog = 0
buiscits = 0
for c in range(1, days + 1):
    dog_food = float(input())
    cat_food = float(input())
    food_eaten_by_cat += cat_food
    food_eaten_by_dog += dog_food
    if c % 3 == 0:
        buiscits += (cat_food + dog_food) * 0.1
eaten_food = food_eaten_by_cat + food_eaten_by_dog
percent_eaten = (food_eaten_by_cat + food_eaten_by_dog) / all_food
percent_eaten_by_dog = food_eaten_by_dog / eaten_food
percent_eaten_by_cat = food_eaten_by_cat / eaten_food
print(f"Total eaten biscuits: {(round(buiscits))}gr.")
print(f"{percent_eaten:.2%} of the food has been eaten.")
print(f"{percent_eaten_by_dog:.2%} eaten from the dog.")
print(f"{percent_eaten_by_cat:.2%} eaten from the cat.")

