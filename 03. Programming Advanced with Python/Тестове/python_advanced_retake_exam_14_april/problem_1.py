from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
pizza_making_capacities = list(map(int, input().split(', ')))
all_pizzas = 0

while pizza_orders and pizza_making_capacities:
    if pizza_orders[0] > 10 or pizza_orders[0] <= 0:
        pizza_orders.popleft()
        continue
    # if pizza_making_capacities[-1] <= 0:
    #     pizza_making_capacities.pop()
    #     continue

    if pizza_orders[0] <= pizza_making_capacities[-1]:
        all_pizzas += pizza_orders.popleft()
        pizza_making_capacities.pop()
    else:

        while pizza_orders[0] > 0 and pizza_making_capacities:
            pizza_orders[0] -= pizza_making_capacities[-1]
            all_pizzas += pizza_making_capacities[-1]
            pizza_making_capacities.pop()
        if pizza_orders[0] <=0:
            all_pizzas -= abs(pizza_orders.popleft())

if len(pizza_orders) == 0:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {all_pizzas}')
    print(f"Employees: {', '.join([str(c) for c in pizza_making_capacities])}")
else:
    print(f'Not all orders are completed.')
    print(f"Orders left: {', '.join([str(c) for c in pizza_orders])}")

