import sys

class Parsing:
	def __init__(self):
		self.user_input = ""
		self.left = ""
		self.right = ""
		self.invalid_syntax = False
		self.variable = {"X^0" : 0, "X^1" : 0 , "X^2" : 0}

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
		print ("X^2 : ", self.variable["X^2"])
		print ("X^1 : ", self.variable["X^1"])
		print ("X^0 : ", self.variable["X^0"])
		print(self.invalid_syntax)

	def __convert_to_int(self):
		for key, value in list(self.variable.items()):
			if value != 0 and value.is_integer():
				self.variable[key] = int(self.variable[key])

	def store_variable(self):
		self.left = self.left.strip().split(" ")
		self.right = self.right.strip().split(" ")

		for i, value in enumerate(self.left):
			for key in self.variable:
				if (value == key and self.left[i - 1] == "*"):
					if i - 3 < 0 or self.left[i - 3] == "+":
						self.variable[key] =  self.variable[key] + float(self.left[i - 2])
					elif self.left[i - 3] == "-":
						self.variable[key] =  self.variable[key] - float(self.left[i - 2])
					else:
						self.invalid_syntax = True

		for i, value in enumerate(self.right):
			for key in self.variable:
				if (value == key and self.right[i - 1] == "*"):
					if i - 3 < 0 or self.right[i - 3] == "+":
						self.variable[key] =  self.variable[key] - float(self.right[i - 2])
					elif self.left[i - 3] == "-":
						self.variable[key] =  self.variable[key] + float(self.right[i - 2])
					else:
						self.invalid_syntax = True

		self.__print_variable()
		self.__convert_to_int()

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

def main():

	parsing_obj = Parsing()
	parsing_obj.get_user_input()
	parsing_obj.check_format()
	if parsing_obj.invalid_syntax == False:
		parsing_obj.split_equality()
	parsing_obj.store_variable()
	print_reduced_form(parsing_obj)

if __name__== "__main__":
  main()
