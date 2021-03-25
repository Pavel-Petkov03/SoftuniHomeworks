import tkinter as tk
from tkinter import messagebox
import random

master = tk.Tk()


def do():
    options_for_town = {
        "Благоевград": random.randint(0, 43),
        "Бургас": random.randint(44, 93),
        "Варна": random.randint(94, 139),
        'Велико Търново': random.randint(140, 169),
        'Видин': random.randint(170, 183),
        'Враца': random.randint(184, 217),
        'Габрово': random.randint(218, 233),
        'Кърджали': random.randint(234, 281),
        'Кюстендил': random.randint(282, 301),
        'Ловеч': random.randint(302, 319),
        'Монтана': random.randint(320, 341),
        'Пазарджик': random.randint(342, 377),
        'Перник': random.randint(378, 395),
        'Плевен': random.randint(396, 435),
        'Пловдив': random.randint(436, 501),
        'Разград': random.randint(502, 527),
        'Русе': random.randint(528, 555),
        'Силистра': random.randint(556, 575),
        'Сливен': random.randint(576, 601),
        'Смолян': random.randint(602, 623),
        'София - град': random.randint(624, 721),
        'София - окръг': random.randint(722, 751),
        'Стара Загора': random.randint(752, 789),
        'Добрич': random.randint(790, 821),
        'Търговище': random.randint(822, 843),
        'Хасково': random.randint(844, 871),
        'Шумен': random.randint(872, 903),
        'Ямбол': random.randint(904, 925),
        'Друг': random.randint(926, 999)
    }
    options_for_month = {
        'Януари': '01',
        'Февруари': '02',
        'Март': '03',
        'Април': '04',
        'Май': '05',
        'Юни': '06',
        'Юли': '07',
        'Август': '08',
        'Септември': '09',
        'Октомври': '10',
        'Ноември': '11',
        'Декември': '12',
    }

    options_for_day = [str(c) if c >= 10 else f'0{c}' for c in range(0, 31)]

    town_bundle = tk.StringVar()
    month_bundle = tk.StringVar()
    day_bundle = tk.StringVar()

    day_bundle.set('Ден')
    month_bundle.set("Месец")
    town_bundle.set("Град")

    def get_month(c):
        if c != 'Месец':
            return options_for_month[c]
        else:
            pass

    def ok():
        initial_year = get_year()
        initial_month = get_month(month_bundle.get())
        initial_day = get_day(day_bundle.get())
        initial_town = get_town_id(town_bundle.get())
        get_final_result(initial_town, initial_day, initial_year, initial_month)

    def get_day(c):
        if str(c)[0] == '0':
            c = f'0{c}'
        return str(c)

    def get_year():
        taken = str(year.get())
        if len(taken) != 4:
            year.delete(0, tk.END)
            year.insert(0, 'Невалидна година')
        else:
            if len(taken) == 1:
                taken = f'00{taken}'
            elif len(taken) == 2:
                taken = f'0{taken}'
            return str(taken)

    def get_town_id(c):
        c = str(options_for_town[c])
        if len(c) == 1:
            c = f'00{c}'
        elif len(c) == 2:
            c = f'0{c}'
        return str(c)

    def get_final_result(t, d, y, m):
        result = ''
        result += y[2:]
        y = int(y)
        if y >= 2000:
            result += f'{int(m) + 40}'
        else:
            result += m
        result += d
        result += t
        final_symbol = int(result[0]) * 2 + int(result[1]) * 4 + int(result[2]) * 8 + int(result[3]) * 5 + int(
            result[4]) * 10 \
                       + int(result[5]) * 9 + int(result[6]) * 7 + int(result[7]) * 3 + int(result[8]) * 6
        final_symbol %= 11
        if final_symbol == 10:
            final_symbol = 0
        result += str(final_symbol)
        year.delete(0, tk.END)
        popup(result)

    def popup(my_idi):
        with open('idi_result.txt', 'w') as file:
            tk.messagebox.showinfo('Вашето Егн е', message=my_idi)

    button = tk.Button(master, text="OK", command=ok)
    month = tk.OptionMenu(master, month_bundle, *options_for_month.keys())
    day = tk.OptionMenu(master, day_bundle, *options_for_day)
    town = tk.OptionMenu(master, town_bundle, *options_for_town.keys())
    year = tk.Entry()
    year.insert(0, 'Година на раждане')

    button.grid(row=3, column=3)
    month.grid(row=2, column=2)
    day.grid(row=2, column=1)
    town.grid(row=2, column=4)
    year.grid(row=2, column=3)

    tk.mainloop()


do()
