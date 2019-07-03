def sqrt(number, number_iters = 500):
	a = float(number)
	for i in range(number_iters):
		number = 0.5 * (number + a / number)
	return number

def print_reduced_form(parsing_obj):
	i = 0
	reduced_form = ("Reduced form: ")
	for key, value in parsing_obj.variable.items():
		if value != 0:
			if (value > 0 and i != 0):
				reduced_form = reduced_form + " + "
			elif (value < 0):
				reduced_form = reduced_form + " - "
				value = -value
			reduced_form = reduced_form + str(value) + " * " + str(key)
			i += 1
	reduced_form = reduced_form + " = 0"
	print (reduced_form)

def print_polynomial_degree(parsing_obj):
	list = []
	for key in parsing_obj.variable:
		list.append(key[2])
	print ("Polynomial degree: " + max(list))
