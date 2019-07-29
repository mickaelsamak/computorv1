import sys
import argparse
from pprint import pprint
import re
#Bonus Plot
import numpy as np
import matplotlib.pyplot as plt

def sqrt(number, number_iters = 500):
	a = float(number)
	for i in range(number_iters):
		number = 0.5 * (number + a / number)
	return number

def check_equality(input):
	if input.count("=") != 1:
		print("Error: An equation must contain (only) one \"=\".")
		exit()

def split_equality(input):
	input = re.sub(r"\s", "", input)
	left, right = input.split("=")
	left = re.sub(
		r"(?P<exp0>(?:^|[+-])(?:\d+\.\d+|\d+)(?!\*|\d+|\.))",
		r"\g<exp0>*X^0",
		left
	)
	left = re.sub(
		r"(?P<exp1>X(?!\^))",
		r"\g<exp1>^1",
		left
	)
	left = re.sub(
		r"(^|[+-])(X\^\d+)",
		r"\g<1>1*\g<2>",
		left
	)
	right = re.sub(
		r"(?P<exp0>(?:^|[+-])(?:\d+\.\d+|\d+)(?!\*|\d+|\.))",
		r"\g<exp0>*X^0",
		right
	)
	right = re.sub(
			r"(?P<exp1>X(?!\^))",
		r"\g<exp1>^1",
		right
	)
	right = re.sub(
		r"(^|[+-])(X\^\d+)",
		r"\g<1>1*\g<2>",
		right
	)
	if not left.strip() or not right.strip():
		print("Error: One side of your equation is empty.")
		exit()
	else:
		return (left, right)

def parse(input):
	terms = {}
	curr_len = 0
	left, right = split_equality(input)
	reg = "(?P<coef>[-+]?\d+\.\d+|[-+]?\d+)\*X\^(?P<exposant>\d+)"
	for match in re.finditer(reg, left):
		if int(match.group('exposant')) in terms:
			terms[int(match.group('exposant'))] = terms[int(match.group('exposant'))] + float(match.group('coef'))
		else:
			terms[int(match.group('exposant'))] = float(match.group('coef'))
		terms[int(match.group('exposant'))] = round(terms[int(match.group('exposant'))], 6)
		curr_len += len(match.group(0))
	for match in re.finditer(reg, right):
		if int(match.group('exposant')) in terms:
			terms[int(match.group('exposant'))] = terms[int(match.group('exposant'))] - float(match.group('coef'))
		else:
			terms[int(match.group('exposant'))] = -float(match.group('coef'))
		terms[int(match.group('exposant'))] = round(terms[int(match.group('exposant'))], 6)
		curr_len += len(match.group(0))
	if curr_len != (len(left) + len(right)):
		print("Error: Invalid Syntax.")
		exit()
	else:
		return (terms)

def print_reduced_form(terms):

	def check_infinite_solution(terms):
		for element in terms:
			if terms[element] != 0:
				return
		print("Reduced form: 0 * X^0 = 0")
		print("Polynomial degree: 0")
		print("Any reel can be the solution.")
		exit()

	reduced_form = ("Reduced form:")
	check_infinite_solution(terms)
	for element in terms:
		if terms[element].is_integer():
			terms[element] = int(terms[element])
		if terms[element] < 0:
			reduced_form = reduced_form + " - " + str(-terms[element]) + " * X^" + str(element)
		if terms[element] > 0:
			if reduced_form != ("Reduced form:") :
				reduced_form = reduced_form + " + " + str(terms[element]) + " * X^" + str(element)
			else:
				reduced_form = reduced_form + " " + str(terms[element]) + " * X^" + str(element)
	reduced_form = reduced_form + " = 0"
	print (reduced_form)

def print_polynomial_degree(terms):
	degree = 0
	for element in terms:
		if int(terms[element]) != 0:
			if element > degree:
				degree = element
	print ("Polynomial degree: " + str(degree))
	return (degree)

def check_invalid(terms):
	for element in terms:
		if element > 2 and terms[element] != 0:
			print("The polynomial degree is stricly greater than 2, I can't solve.")
			exit()
	invalid = False
	for element in terms:
		if element == 0 and terms[element] != 0:
			invalid = True
		if element != 0 and terms[element] != 0:
			invalid = False
	if invalid == True:
		print ("Error: Equality is not correct")
		exit()

def check_empty_terms(terms):
	if 0 not in terms.keys():
		terms[0] = 0
	if 1 not in terms.keys():
		terms[1] = 0
	if 2 not in terms.keys():
		terms[2] = 0
	return (terms)

def reduce(x):
	x = float(x)
	x = round(x, 6)
	if x.is_integer():
		x = int(x)
	return (x)

def plot_bonus(a, b, c):
	#Bonus Plot
	x = np.linspace(-50, 50, 256, endpoint = True)
	y = (a * (x * x)) + (b * x) + c

	plt.plot(x, y)

	axes = plt.gca()
	axes.set_xlim([x.min(), x.max()])
	axes.set_ylim([y.min(), y.max()])

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Polynomial Curve')

	plt.show()

def play(terms, degree):
	c,b,a = terms[0], terms[1], terms[2]
	if degree == 1:
		solution = reduce(-c/b)
		print("Solution is :")
		print(str(solution) + " or " + str(-c) + "/" + str(b))
	if degree == 2:
		delta = reduce(b * b - (4 * a * c))
		print ("Calculate of Discriminant:")
		print ("Δ = " + str(delta))
		if delta > 0:
			print ("Discriminant is strictly positive, the two solutions are:")
			solution1 = reduce((-b - sqrt(delta)) / (2 * a))
			solution2 = reduce((-b + sqrt(delta)) / (2 * a))
			print(str(solution1) + " or " + str(-b) + " - √" + str(delta) + " /" + str(2 * a))
			print(str(solution2) + " or " + str(-b) + " + √" + str(delta) + " /" + str(2 * a))
		if delta == 0:
			print("Discriminant == 0, the solution is:")
			solution1 = reduce(-b / (2 * a))
			print(str(solution1) + " or " + str(-b) +" / " + str(2 * a))
		if delta < 0:
			print("Discriminant is strictly negative, the two complex solutions are:")
			solution1 = str(reduce(-b/2*a)) + "-" + str(reduce(sqrt(-delta)/2*a)) + "i"
			solution2 = tr(reduce(-b/2*a)) + "+" + str(reduce(sqrt(-delta)/2*a)) + "i"
			print(solution1 + " or " + str(-b) + " - i√" + str(-delta) + " /" + str(2 * a))
			print(solution2 + " or " + str(-b) + " + i√" + str(-delta) + " /" + str(2 * a))
	plot_bonus(a, b ,c)
	exit()

def solve(input):
	check_equality(input)
	terms = parse(input)
	print_reduced_form(terms)
	degree = print_polynomial_degree(terms)
	check_invalid(terms)
	terms = check_empty_terms(terms)
	play(terms, degree)

def get_user_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("equation", help="Solve Polynomial Equation")
	args = parser.parse_args()
	return (args.equation)

def main():
	input = get_user_input()
	solve(input)

if __name__== "__main__":
  main()
