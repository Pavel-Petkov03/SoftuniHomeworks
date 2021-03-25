budget = float(input())
cozonac_count = 0
eggs = 0
price_for_kg_flour = float(input())
price_for_pack_of_eggs = 0.75 * price_for_kg_flour
price_for_250ml_milk = (price_for_kg_flour * 1.25) / 4
cozonac = price_for_kg_flour + price_for_pack_of_eggs + price_for_250ml_milk
while budget > cozonac:
    budget -= cozonac
    cozonac_count += 1
    eggs += 3
    if cozonac_count % 3 == 0:
        eggs -= cozonac_count - 2
print(f"You made {cozonac_count} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")

