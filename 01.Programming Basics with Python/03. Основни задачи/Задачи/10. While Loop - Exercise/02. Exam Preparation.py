# Напишете програма, в която Марин решава задачи от изпити,
# докато не получи съобщение "Enough" от лектора си. При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда "Enough" или ако
# Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка,
# която е по-малка или равна на 4.
# Вход
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6].
# Изход
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
unsatisfactory_grades = int(input())
massage = input()
poor_grade = 0
count_ex = 0
average = 0
last_ex = ''
while massage != "Enough":
    grade = float(input())
    count_ex += 1
    average += grade
    if grade <= 4:
        poor_grade += 1
    last_ex = massage
    if unsatisfactory_grades == poor_grade:
        print(f"You need a break, {poor_grade} poor grades.")
        break
    massage = input()
else:
    print(f"Average score: {(average / count_ex):.2f}")
    print(f"Number of problems: {count_ex}")
    print(f"Last problem: {last_ex}")


