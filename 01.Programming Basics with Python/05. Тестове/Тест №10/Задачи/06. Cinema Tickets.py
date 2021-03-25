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
command = input()
student = 0
standard = 0
kid = 0
counter_for_movie = 0
total_tickets = 0
while command != "Finish":
    seats = int(input())
    for c in range(1 , seats + 1):
        type = input()
        if type == "End":
            break
        if type == "student":
            student += 1
        elif type == "standard":
            standard += 1
        elif type == "kid":
            kid += 1
        counter_for_movie += 1
        total_tickets += 1
    print(f"{command} - {(counter_for_movie / seats * 100):.2f}% full.")
    counter_for_movie = 0
    command = input()
print(f"Total tickets: {total_tickets}")
print(f"{(student /total_tickets *100):.2f}% student tickets.")
print(f"{(standard / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kid / total_tickets * 100):.2f}% kids tickets.")
