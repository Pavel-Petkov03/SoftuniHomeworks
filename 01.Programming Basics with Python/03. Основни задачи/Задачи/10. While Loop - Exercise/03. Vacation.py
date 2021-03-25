# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере
# дали ще успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."
needed_money = float(input())
money = float(input())
days_all = 0
spend_times = 0
while needed_money > money and spend_times < 5:
    command = input()
    days_all += 1
    intake_money = float(input())
    if command == "spend":
        money -= intake_money
        spend_times += 1
    elif command == "save":
        spend_times = 0
        money += intake_money
    if money < 0:
        money = 0
else:
    if needed_money <= money:
        print(f"You saved the money for {days_all} days.")
    if spend_times == 5:
        print( f"You can't save the money." )
        print( f"{days_all}" )




