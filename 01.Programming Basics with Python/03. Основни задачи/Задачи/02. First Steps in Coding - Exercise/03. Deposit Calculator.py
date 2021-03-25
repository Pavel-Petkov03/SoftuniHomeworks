# Трябва да се сметне депозит(сума) спрямо три величини: срок за депозита, депозитен лихвен процент , годишен лихвен
# процент. Сумата е равна на депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
dep_sum = float(input())
deposit_session = int(input())
year_interest_percent = float(input())
sum_d = dep_sum + deposit_session * ((dep_sum * year_interest_percent/100)/12)
print(sum_d)