# Write a program that converts British pounds to US dollars formatted to the 3th decimal point.
# 1 British Pound = 1.31 Dollars
pounds = int(input())
dollars = pounds * 1.31
print(f'{dollars:.3f}')
