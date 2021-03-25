from tk_logic import *



def button_creation():
	button_1 = Button(root, text='1', pady=40, padx=40, command = lambda: button_getting_function(1))
	button_2 = Button(root, text='2', pady=40, padx=40,command = lambda: button_getting_function(2))
	button_3 = Button(root, text='3', pady=40, padx=40,command = lambda: button_getting_function(3))
	button_4 = Button(root, text='4', pady=40, padx=40,command=lambda: button_getting_function(4))
	button_5 = Button(root, text='5', pady=40, padx=40,command=lambda: button_getting_function(5))
	button_6 = Button(root, text='6', pady=40, padx=40,command=lambda: button_getting_function(6))
	button_7 = Button(root, text='7', pady=40, padx=40, command=lambda: button_getting_function(7))
	button_8 = Button(root, text='8', pady=40, padx=40, command=lambda: button_getting_function(8))
	button_9 = Button(root, text='9', pady=40, padx=40,command=lambda: button_getting_function(9))
	button_0 = Button(root, text='0', pady=40, padx=41,command=lambda: button_getting_function(0))

	binary = Button(root, text='bin', pady=40, padx=40,command=lambda: binary_button())
	button_add = Button(root, text='+', pady=40, padx=40,command=lambda: button_getting_function('+'))
	button_subtract = Button(root, text='-', pady=40, padx=40,command=lambda: button_getting_function('-'))
	button_divide = Button(root, text='/', pady=40, padx=40,command=lambda: button_getting_function('/'))
	button_multiply = Button(root, text='*', pady=40, padx=40,command=lambda: button_getting_function('*'))

	button_even = Button(root, text='=', pady=40, padx=40,command=lambda: equals_button())
	button_clear = Button(root, text='C', pady=40, padx=40,command=lambda: clear_button())

	# memory_button = Button(root, text='memory', pady=40, padx=40,command=lambda: open_memory())

	button_idi = Button(root, text='C', pady=40, padx=40,command=1)

	button_1.grid( row=4, column=1 )
	button_2.grid( row=4, column=2)
	button_3.grid( row=4, column=3)

	button_4.grid( row=3, column=1)
	button_5.grid( row=3, column=2)
	button_6.grid( row=3, column=3)

	button_7.grid( row=2, column=1)
	button_8.grid( row=2, column=2)
	button_9.grid( row=2, column=3)

	button_0.grid( row=5, column=1)
	button_add.grid( row=3, column=4)
	button_subtract.grid( row=5, column=4)
	button_divide.grid( row=2, column=4)
	button_even.grid( row=5, column=3)
	button_multiply.grid(row=4, column=4)

	button_clear.grid( row=5, column=2 )
	# memory_button.grid( row=6, column=5 )
	binary.grid( row=6, column=3 )

	button_idi.grid(row=5,column=5)


button_creation()



