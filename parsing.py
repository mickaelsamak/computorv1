import sys
from pprint import pprint
from tools import *

class Parsing:
	def __init__(self):
		self.user_input = ""
		self.left = ""
		self.right = ""
		self.invalid_syntax = False
		self.variable = {}

	def get_user_input(self):
		if len(sys.argv) == 2:
			self.user_input = sys.argv[1]
		else:
			invalid_syntax = True

	def check_format(self):
		if self.user_input.count('=') is not 1:
			self.invalid_syntax = True

	def split_equality(self):
		self.left, self.right = self.user_input.split("=")

	def __print_variable(self):
		pprint (self.variable)

	def __convert_to_int(self):
		for key, value in list(self.variable.items()):
			if value != 0 and value.is_integer():
				self.variable[key] = int(self.variable[key])

	def store_variable(self, max = 10):
		self.left = self.left.strip().split(" ")
		self.right = self.right.strip().split(" ")

		for i, value in enumerate(self.left):
			for j in range(max):
				if (value == "X^" + str(j) and self.left[i - 1] == "*"):
					if "X^" + str(j) not in self.variable.items():
						self.variable["X^" + str(j)] = 0
					if i - 3 < 0 or self.left[i - 3] == "+":
						self.variable["X^" + str(j)] =  self.variable["X^" + str(j)] + float(self.left[i - 2])
					elif self.left[i - 3] == "-":
						self.variable["X^" + str(j)] =  self.variable["X^" + str(j)] - float(self.left[i - 2])
					else:
						self.invalid_syntax = True

		for i, value in enumerate(self.right):
			for j in range(max):
				if (value == "X^" + str(j) and self.right[i - 1] == "*"):
					if "X^" + str(j) not in self.variable.items():
						self.variable["X^" + str(j)] = 0
					if i - 3 < 0 or self.right[i - 3] == "+":
						self.variable["X^" + str(j)] =  self.variable["X^" + str(j)] - float(self.right[i - 2])
					elif self.left[i - 3] == "-":
						self.variable["X^" + str(j)] =  self.variable["X^" + str(j)] + float(self.right[i - 2])
					else:
						self.invalid_syntax = True

		self.__print_variable()
		self.__convert_to_int()
