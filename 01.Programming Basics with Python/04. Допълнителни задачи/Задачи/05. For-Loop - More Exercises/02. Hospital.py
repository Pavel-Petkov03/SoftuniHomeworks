# За даден период от време, всеки ден в болницата пристигат пациенти за преглед.
# Тя разполага първоначално със 7 лекари. Всеки лекар може да преглежда само по един пациент на ден,
# но понякога има недостиг на лекари, затова останалите пациенти се изпращат в други болници. Всеки трети ден,
# болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям от броя на прегледаните,
# се назначава още един лекар. Като назначаването става преди да започне приемът на пациенти за деня.
# Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
# Вход
# Входът се чете от конзолата и съдържа:
# •	На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# •	На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден.
# Цяло число в интервала [0…10 000]
# Изход
# Да се отпечатат на конзолата 2 реда :
# •	На първия ред: "Treated patients: {брой прегледани пациенти}."
# •	На втория ред: "Untreated patients: {брой непрегледани пациенти}."
days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
all_treated_patients = 0
for b in range(1 , days + 1):
    patients = int(input())
    if b % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if doctors <= patients:
        all_treated_patients += doctors
        treated_patients = doctors
        untreated_patients += patients - treated_patients
    else:
        all_treated_patients += patients
        treated_patients = patients
        untreated_patients += patients - treated_patients

print(f'Treated patients: {all_treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')







