print("Lets try - Try and Exception")

def calculate(number):
	print("Number is : ", number)

	try:
		value = 12/number

	except ArithmeticError:
		print("It is an Arithmetic Error with input number", number)
	except Exception:
		print("There is an exception with input number", number)

calculate(3)
calculate(0)