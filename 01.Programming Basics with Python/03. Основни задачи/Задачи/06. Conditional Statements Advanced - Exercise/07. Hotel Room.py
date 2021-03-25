# Хотел предлага 2 вида стаи: студио и апартамент.
# Напишете програма, която изчислява цената за целия престой за студио и апартамент.
# Цените зависят от месеца на престоя:
# Май и октомври	Юни и септември	Юли и август
# Студио – 50 лв./нощувка	Студио – 75.20 лв./нощувка	Студио – 76 лв./нощувка
# Апартамент – 65 лв./нощувка	Апартамент – 68.70 лв./нощувка	Апартамент – 77 лв./нощувка
# Предлагат се и следните отстъпки:
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# •	На първия ред е месецът – May, June, July, August, September или October;
# •	На втория ред е броят на нощувките – цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
# •	На първия ред: "Apartment: {цена за целият престой} lv."
# На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
month = input()
nights = int(input())
studio = float()
apartment = float()
if month == "May" or month == "October":
    studio = nights * 50
    apartment = nights * 65
elif month == "June" or month == "September":
    studio = nights * 75.2
    apartment = nights * 68.70
elif month == "July" or month == "August":
    studio = nights * 76
    apartment = nights * 77
if month == "May" or month == "October":
    if nights > 14:
        studio = studio - 0.3 * studio
    elif nights > 7:
        studio = studio - 0.05 * studio
if nights > 14 and month == "June" or month == "September":
    studio = studio - 0.2 * studio
if nights > 14:
    apartment = apartment - 0.1 * apartment
print(f'Apartment: {apartment:.2f} lv.')
print(f"Studio: {studio:.2f} lv.")