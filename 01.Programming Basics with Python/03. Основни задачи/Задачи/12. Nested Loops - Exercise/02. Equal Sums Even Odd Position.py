# Напишете програма, която чете от конзолата две шестцифрени цели числа в диапазона. Винаги първото въведено число ще бъде по-малко от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете, прочетени от конзолата числа, и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни. Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.
smaller_n = int(input())
bigger_n = int(input())
for numbers in range(smaller_n , bigger_n + 1):
    symbols = str(numbers)
    odd_sum = 0
    even_sum = 0
    for index ,  digit in enumerate(symbols):
        if index % 2:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(symbols , end = ' ')




