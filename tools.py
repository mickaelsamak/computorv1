def sqrt(number, number_iters = 500):
	a = float(number)
	for i in range(number_iters):
		number = 0.5 * (number + a / number)
		print (number)
	return number
