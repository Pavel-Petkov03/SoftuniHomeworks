def stock_availability(stocks: list, *another):
    if another[0] == 'delivery':
        for item in another[1:]:
            stocks.append(item)
    elif another[0] == 'sell':
        if len(another) > 1 and isinstance(another[1], int):
            for _ in range(another[1]):
                stocks.pop(0)
        elif len(another) > 1:
            for item in another[1:]:
                if item in stocks:
                    for s in range(stocks.count(item)):
                        stocks.remove(item)
        else:
            stocks.pop(0)
    return stocks

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



