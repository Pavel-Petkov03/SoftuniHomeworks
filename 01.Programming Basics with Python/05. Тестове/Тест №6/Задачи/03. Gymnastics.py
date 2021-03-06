# На световно първенство по художествена гимнастика три от държавите се изявяват като лидери в класирането
# (Русия, България, Италия). Вашата задача е да изчислите каква е оценката дадена от журито за конкретно съчетание,
# като знаете държавата, която е играла и с кой уред е играла - лента, обръч или въже. За съчетанието си, отбора е
# получил две оценки: оценка за трудност и оценка за изпълнение на съчетанието, като крайната оценка е
# сбор на двете оценки. В таблицата са показани какви оценки за трудност и изпълнение
# са получили ансамблите за всеки един уред.
# Уред	Русия	България	Италия
# Лента(ribbon)	Трудност: 9.100
# Изпълнение: 9.400	Трудност: 9.600
# Изпълнение: 9.400	Трудност: 9.200
# Изпълнение: 9.500
# Обръч(hoop)	Трудност: 9.300
# Изпълнение: 9.800	Трудност: 9.550
# Изпълнение: 9.750	Трудност: 9.450
# Изпълнение: 9.350
# Въже(rope)	Трудност: 9.600
# Изпълнение: 9.000	Трудност: 9.500
# Изпълнение: 9.400	Трудност: 9.700
# Изпълнение: 9.150
# Напишете програма, която изчислява каква е оценката на дадена
# държава за определен уред и колко процента не им достигат,
# за да имат максималната оценка, която е 20.
# Вход
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# •	Втори ред – уред - текст ("ribbon", "hoop" или "rope")
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	Първи ред: "The team of {държава} get {обща оценка} on {уред}."
# •	Втори ред:  "{процентът, който не им достига до максималния брой точки}%"
# Общата оценка да бъде форматирана до третата цифра след десетичния знак, а процентът да бъде форматиран до втората
# цифра след десетичния знак.
country = input()
weapon = input()
hardness = 0
performance = 0
if country == "Russia":
    if weapon == "ribbon":
        hardness = 9.1
        performance = 9.40
    elif weapon == "hoop":
        hardness = 9.3
        performance = 9.8
    elif weapon == "rope":
        hardness = 9.6
        performance = 9
elif country == "Bulgaria":
    if weapon == "ribbon":
        hardness = 9.6
        performance =  9.4
    elif weapon == "hoop":
        hardness = 9.55
        performance = 9.75
    elif weapon == "rope":
        hardness = 9.5
        performance = 9.4
elif country == "Italy":
    if weapon == "ribbon":
        hardness = 9.2
        performance = 9.5
    elif weapon == "hoop":
        hardness = 9.45
        performance = 9.35
    elif weapon == "rope":
        hardness = 9.7
        performance = 9.15
all_points = hardness + performance
print(f"The team of {country} get {all_points:.3f} on {weapon}.")
print(f"{(((20 - all_points) / 20) * 100):.2f}%")







