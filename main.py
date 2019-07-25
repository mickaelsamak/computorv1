import sys
import argparse
from pprint import pprint
import re
from tools import *

def check_equality(input):
	if input.count("=") != 1:
		print("Error: An equation must contain (only) one \"=\".")
		exit()

def split_equality(input):
	input = re.sub(r"\s", "", input)
	left, right = input.split("=")
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
		terms[int(match.group('exposant'))] = float(match.group('coef'))
		curr_len += len(match.group(0))
	for match in re.finditer(reg, right):
		if int(match.group('exposant')) in terms:
			terms[int(match.group('exposant'))] = terms[int(match.group('exposant'))] - float(match.group('coef'))
		else:
			terms[int(match.group('exposant'))] = -float(match.group('coef'))
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

def solve(input):
	check_equality(input)
	terms = parse(input)
	print_reduced_form(terms)
	degree = print_polynomial_degree(terms)
	check_invalid(terms)
	terms = check_empty_terms(terms)
	if degree == 2:
		c,b,a = terms[0], terms[1], terms[2]
		delta = b * b - (4 * a * c)
		print ("Calculate of Discriminant:")
		print ("Δ = " + str(delta))
		if delta > 0:
			print ("Discriminant is strictly positive, the two solutions are:")
			solution1 = (-b - sqrt(delta)) / (2 * a)
			solution2 = (-b + sqrt(delta)) / (2 * a)
			print(solution1)
			print(solution2)
			print ("Solution 1 : " + str(-b) + " - √" + str(delta) + " /" + str(2 * a))
			print ("Solution 2 : " + str(-b) + " + √" + str(delta) + " /" + str(2 * a))
		if delta == 0:
			print("Discriminant == 0, the solution is:")
			solution1 = -b / (2 * a)
			print(solution1)
			print ("Fraction : " + str(-b) +" / " + str(2 * a))
		if delta < 0:
			print("Discriminant is strictly negative, the two complex solutions are:")


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
