# Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех.
# Изискване за социална стипендия -
# доход на член от семейството по-малък от минималната работна заплата и успех над 4.5.
# Размер на социалната стипендия - 35% от минималната работна заплата.
# Изискване за стипендия за отличен успех - успех над 5.5, включително.
# Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.
# Напишете програма, която при въведени доход, успех и минимална работна заплата,
# дава информация дали ученик има право да получава стипендия, и стойността на стипендията, която е по-висока за него.
# Вход
# Потребителят въвежда 3 числа, по едно на ред:
# 1.	Доход в лева - реално число;
# 2.	Среден успех -  реално числсо;
# 3.	Минимална работна заплата – реално число.
# Изход
# 	Ако ученикът няма право да получава стипендия, се извежда:
# "You cannot get a scholarship!"
# Ако ученикът има право да получава само социална стипендия:
# "You get a Social scholarship {стойност на стипендия} BGN"
# Ако ученикът има право да получава само стипендия за отличен успех:
# "You get a scholarship for excellent results {стойност на стипендията} BGN"
# Ако ученикът има право да получава и двата типа стипендии, ще получи по-голямата по сума,
# а ако са равни ще получи тази за отличен успех.
income_money = float(input())
average = float(input())
minimal_salary = float(input())
excellent = average * 25
low_money = minimal_salary * 0.35
if income_money < minimal_salary and average >= 5.50:
    if low_money > excellent:
        print(f"You get a Social scholarship {int(low_money)} BGN")
    else:
        print(f'You get a scholarship for excellent results {int(excellent)} BGN')
elif income_money < minimal_salary and average > 4.50:
    print(f"You get a Social scholarship {int(low_money)} BGN")
elif average >= 5.50:
    print(f'You get a scholarship for excellent results {int(excellent)} BGN')
else:
    print("You cannot get a scholarship!")


