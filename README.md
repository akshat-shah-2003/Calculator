# Calculator
Imports used:
Kivy

Simple calculator with "+","-","*","/", operations. eval() function is used to calculate expression result.

Special use of lambda function for input, to avoid multiple functions for input of each symbol or number.

For example: 

self.button8.bind(on_press=lambda x: self.appen("1",x)) # to input "1" in the text box
self.button9.bind(on_press=lambda x: self.appen("2",x)) # to input "2" in the text box
self.button10.bind(on_press=lambda x: self.appen("3",x)) # to input "3" in the text box

Note: here, appen() function takes an argument and appends it in the text box
