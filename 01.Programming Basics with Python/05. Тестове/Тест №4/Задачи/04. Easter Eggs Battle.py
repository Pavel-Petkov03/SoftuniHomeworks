# На Великден семейството на Деси се събира и тя решава да организира "битка" между великденски яйца.
# Правилата на "битката" са следните:
# •	Участват двама играчи
# •	Всеки от тях започва с определен брой яйца
# •	При получаване на команда "one" -> първият играч печели => яйцата на втория намаляват с едно
# •	При получаване на команда "two" -> вторият играч печели => яйцата на първия намаляват с едно
# •	Играта приключва, ако някой от играчите остане без яйца или до получаване на команда "End of battle"
# Вход
# Първоначално се четат два реда:
# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
# След това до получаване на команда "End of battle" се четe многократно един ред:
# 3.	Победител - текст - "one" или "two"
# Изход
# Ако първият играч остане без яйца:
# •	"Player one is out of eggs. Player two has {брой останали яйца на втория играч} eggs left."
# Ако вторият играч остане без яйца:
# •	"Player two is out of eggs. Player one has {брой останали яйца на първия играч} eggs left."
# При команда "End of battle" да се отпечатат два реда:
# •	"Player one has {брой останали яйца на първия играч} eggs left."
# •	"Player two has {брой останали яйца на втория играч} eggs left."
first_player_eggs = int(input())
second_player_eggs = int(input())
command = input()
is_1_out = False
is_2_out = False
while command != "End of battle":
    if command == "one":
        second_player_eggs -= 1
    elif command == "two":
        first_player_eggs -= 1
    if first_player_eggs == 0 or second_player_eggs == 0:
        if first_player_eggs == 0:
            is_1_out = True
            break
        else:
            is_2_out = True
            break
    command = input()
if is_1_out:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif is_2_out:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")