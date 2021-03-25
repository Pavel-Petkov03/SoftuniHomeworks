# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.
input_hours = int(input())
input_minutes = int(input())
time_after_15_minutes = input_hours * 60 + input_minutes + 15
actual_minutes = time_after_15_minutes % 60
actual_hours = time_after_15_minutes // 60
if actual_hours >= 24:
    if actual_minutes < 10:
        print(f'0:0{actual_minutes}')
    else:
        print(f'{0}:{actual_minutes}')
else:
    if actual_minutes < 10:
        print(f'{actual_hours}:0{actual_minutes}')
    else:
        print(f'{actual_hours}:{actual_minutes}')

