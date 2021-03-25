
# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа. Напишете програма,
# която проверява дали всички двойки имат еднаква стойност или печата максималната разлика между две
# последователни двойки. Аковсички двойки имат еднаква стойност, отпечатайте "Yes, value = {Value}" + стойността.
# В противен случай отпечатайте "No, maxdiff = {Difference}" + максималната разлика.
n = int(input())
is_all_equal = True
current_sum = 0
previous_sum = 0
biggest_difference_between_two_couples = 0
for numbers in range(1, 2 * n + 1):
    number = int(input())
    if numbers % 2 == 0:
        current_sum += number
        if numbers == 2:
            previous_sum = current_sum
        else:
            if current_sum != previous_sum:
                is_all_equal = False
        difference_between_last_two_couples = abs(current_sum - previous_sum)
        if difference_between_last_two_couples > biggest_difference_between_two_couples:
            biggest_difference_between_two_couples = abs(difference_between_last_two_couples)
        previous_sum = current_sum
        current_sum = 0
    else:
        current_sum += number
if is_all_equal:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={biggest_difference_between_two_couples}")
    






