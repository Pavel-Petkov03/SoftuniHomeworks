# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o	Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# •	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# •	При получаване на командата "Finish" да се отпечатат четири реда:
# o	"Total tickets: {общият брой закупени билети за всички филми}"
# o	"{процент на студентските билети}% student tickets."
# o	"{процент на стандартните билети}% standard tickets."
# o	"{процент на детските билети}% kids tickets."
film = input()
people_in_the_hall = 0
student = 0
standard = 0
kid = 0
all_people = 0
while film != "Finish":
    hall_capacity = int(input())
    watcher = input()
    while watcher != "End":
        people_in_the_hall += 1
        all_people += 1
        if watcher == "kid":
            kid += 1
        elif watcher == "student":
            student += 1
        elif watcher == "standard":
            standard += 1
        if hall_capacity == people_in_the_hall:
            break
        watcher = input()
    print(f"{film} - {(people_in_the_hall / hall_capacity * 100):.2f}% full.")
    people_in_the_hall = 0
    film = input()
print(f"Total tickets: {all_people}")
print(f"{(student / all_people * 100):.2f}% student tickets.")
print(f"{(standard / all_people * 100):.2f}% standard tickets.")
print(F"{(kid / all_people * 100):.2f}% kids tickets.")




