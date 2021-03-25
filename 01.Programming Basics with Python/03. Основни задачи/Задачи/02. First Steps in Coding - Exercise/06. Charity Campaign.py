# Трябва да разберем колко пари ще получим от една сладкарница ако вкараме в конзолата няколко величини а те са:
# Колко дни ще тече приготвянето , количеството на тортите, гофретите, палачинките и сладарите.
days_for_the_company = int(input())
bakers = days_for_the_company * int(input())
count_of_cakes = int(input()) * 45
count_of_waffles = int(input()) * 5.80
pancakes = int(input()) * 3.20
income_sum = bakers * (count_of_cakes + count_of_waffles + pancakes)
outcome_sum = income_sum/8
final_sum = income_sum - outcome_sum
print(final_sum)
