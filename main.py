import sys
import argparse
from pprint import pprint
import re

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
			terms[int(match.group('exposant'))] = terms[int(match.group('exposant'))] -float(match.group('coef'))
		else:
			terms[int(match.group('exposant'))] = -float(match.group('coef'))
		curr_len += len(match.group(0))
	if curr_len != (len(left) + len(right)):
		print("Error: Invalid Syntax.")
		exit()
	else:
		return (terms)

def solve(input):
	check_equality(input)
	terms = parse(input)

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
