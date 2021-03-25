# Напишете програма, която изчислява колко часове ще са необходими на един архитект,
# за да изготви проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.
# Вход
# От конзолата се четат 2 реда:
# 1.	Името на архитекта - текст;
# 2.	Брой на проектите - цяло число


architect_name = input()
count_of_projects = int(input())
hours = count_of_projects * 3
print(f'The architect {architect_name} will need {hours} hours to complete {count_of_projects} project/s.')
