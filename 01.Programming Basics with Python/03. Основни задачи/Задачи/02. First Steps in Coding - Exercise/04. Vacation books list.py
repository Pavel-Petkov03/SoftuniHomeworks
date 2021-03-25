# Трябва да се сметне колко часа на ден трябва да чете Жоро ако имаме страниците на книгата,страници които може да
# прочита за един час и дните за които трябва да ги прочете:
page_num = int(input())
pages_for_hour = int(input())
days_he_can_read = int(input())
hours_per_day = (page_num/pages_for_hour)/days_he_can_read
print(hours_per_day)