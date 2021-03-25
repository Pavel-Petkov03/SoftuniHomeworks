from itertools import combinations
from tkinter import *
from collections import deque
from id_logic import *
import os
root = Tk()
root.geometry('409x548-10-10')

e = Entry(width=80, borderwidth=5)
e.grid(row=0, column=0, columnspan=35)


def clear_button():
	e.delete(0, END)


def division_error(our_user_input):
	for index in range(len(our_user_input)-1):
		if our_user_input[index] == '/' and our_user_input[index+1] == '0':
			return True
	return False


def button_getting_function(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, current + str(number))


def finding_error(our_user_input):
	template = ['+', '-', '*','/']
	if our_user_input:
		if our_user_input[-1] in template or our_user_input[0] in template or division_error(our_user_input):
			return True
		for error in set(combinations(['+', '-', '*','/','+', '-', '*','/'], 2)):
			if ''.join(error) in our_user_input:
				return True
		return False


def equals_button():
	current_state = e.get()
	# memory_(current_state)
	if finding_error(current_state):
		e.delete(0, END)
		e.insert(0,'Invalid Input')
	else:
		if current_state:
			number = eval(current_state)
			e.delete(0, END)
			e.insert(0, number)


def binary_to_decimal_convert(decimal_code):
	result = []
	num = int(decimal_code)
	while num != 0:
		if num % 2 == 1:
			result.append(1)
		else:
			result.append(0)
		num //= 2
	return ''.join(reversed(list(map(str, result))))


def binary_button():
	current_word = e.get()
	e.delete(0,END)
	try:
		current_digit = int(current_word)
		e.insert(0, binary_to_decimal_convert(current_digit))
	except ValueError:
		current_word = deque([char for char in current_word])
		final_result = []
		while current_word:
			current_char = current_word[0]
			char_represented_by_nums = ord(current_char)
			final_result.append(binary_to_decimal_convert(char_represented_by_nums))
			current_word.popleft()

		e.delete(0, END)
		e.insert(0, ' '.join(reversed(list(map(str, final_result)))))


def idi_action():
	do()


# def memory_(text):
# 	with open('memory.txt', 'a') as file:
# 		file.writelines(f"{text}\n")


# def open_memory():
# 	e.delete(0, END)
# 	with open('memory.txt', 'r') as file:
# 		text = ' '.join(file.readlines())
# 	e.insert(0, text)


