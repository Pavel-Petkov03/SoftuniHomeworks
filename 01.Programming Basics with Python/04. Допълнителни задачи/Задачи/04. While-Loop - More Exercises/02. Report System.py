# На благотворително събитие плащанията за закупените продукти винаги се редуват:
# плащане в брой и плащане с карта. Установени са следните правила за заплащане:
# •	Ако продуктът надвишава 100лв., за него не може да се плати в брой
# •	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
# •	Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
# цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
# •	При успешна транзакция: "Product sold!"
# •	При неуспешна транзакция: "Error in transaction!"
# •	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума,
# програмата трябва да приключи и на конзолата да се изпишат два реда:
# o	"Average CS: {средно плащане в кеш на човек}"
# o	"Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# •	При получаване на команда "End", да се изпише един ред:
# o	"Failed to collect required money for charity."
reach_sum = int(input())
transaction = input()
card = 0
cash = 0
compiled_money = 0
times = 0
card_count = 0
cash_count = 0
it_is_bigger = False
while transaction != "End":
    times += 1
    transaction = int(transaction)
    if times % 2 == 0:
        if transaction < 10:
            print("Error in transaction!")
        else:
            card += transaction
            card_count += 1
            print("Product sold!")
    else:
        if transaction > 100:
            print("Error in transaction!")
        else:
            cash += transaction
            print("Product sold!")
            cash_count += 1
    compiled_money = cash + card
    if compiled_money >= reach_sum:
        it_is_bigger = True
        break
    transaction = input()
if it_is_bigger:
    print(f"Average CS: {(cash/ cash_count):.2f}")
    print(f"Average CC: {(card / card_count):.2f}")
else:
    print("Failed to collect required money for charity.")



