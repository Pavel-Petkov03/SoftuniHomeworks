def transfer_from_encrypted_to_normal(t):
    t = t.split(':')
    t = [v for v in t if v]
    if len(t) < 3:
        for _ in range(3 - len(t)):
            t.insert(0, 0)
    return t


def format_from_actual_to_encrypted(result_time):
    if result_time[0] <= 9:
        result_time[0] = f'0{result_time[0]}'
    if result_time[2] == 0:
        result_time.pop()
    actual_result = f'{result_time[2]}::{result_time[1]}:{result_time[0]}' if len(
        result_time) == 3 else f'{result_time[1]}:{result_time[0]}'
    return actual_result


my_time_list = [0, 0, 0]
time1 = list(map(int, reversed(transfer_from_encrypted_to_normal(input()))))
time2 = list(map(int, reversed(transfer_from_encrypted_to_normal(input()))))
for index in range(len(time1)):
    new = time1[index] + time2[index]
    if index == 0:
        if new >= 60:
            my_time_list[index + 1] += new // 60
            my_time_list[index] += new % 60
        else:
            my_time_list[index] += new
    elif index == 1:

        if new + my_time_list[index] >= 24:
            my_time_list[index + 1] += (new + my_time_list[index]) // 24
            my_time_list[index] = (new + my_time_list[index]) % 24
        else:
            my_time_list[index] += new
    else:
        my_time_list[index] += new

print(format_from_actual_to_encrypted(my_time_list))
# first verion of the programm, I am going to make it with datetime
# converting the time into sum with regex
# PASS
