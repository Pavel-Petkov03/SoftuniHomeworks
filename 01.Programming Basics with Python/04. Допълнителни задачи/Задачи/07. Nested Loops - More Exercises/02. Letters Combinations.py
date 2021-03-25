# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.
first_letter = input()
second_letter = input()
except_letter = input()
counter = 0
for first in range(ord(first_letter) , ord(second_letter) + 1):
    first = chr(first)
    for second in range( ord( first_letter ), ord( second_letter ) + 1 ):
        second = chr(second)
        for third in range( ord( first_letter ), ord( second_letter ) + 1 ):
            third = chr(third)
            if first != except_letter and second != except_letter and third != except_letter:
                counter += 1
                print(f'{first}{second}{third}' , end=' ')
print(counter)




