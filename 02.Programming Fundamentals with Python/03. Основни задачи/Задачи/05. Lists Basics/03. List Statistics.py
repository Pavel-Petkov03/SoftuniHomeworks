# You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
n = int(input())
positive = []
negative = []
count = 0
sum_negative = 0
for i in range(1 , n + 1):
    num = int(input())
    if num >= 0:
        positive.append(num)
        count += 1
    else:
        negative.append(num)
        sum_negative += num
print(positive)
print(negative)
print(f'Count of positives: {count}. Sum of negatives: {sum_negative}')
