from tools import *
from parsing import *

def main():

	parsing_obj = Parsing()
	parsing_obj.get_user_input()
	parsing_obj.check_format()
	if parsing_obj.invalid_syntax == False:
		parsing_obj.split_equality()
	parsing_obj.store_variable()
	print_reduced_form(parsing_obj)
	print_polynomial_degree(parsing_obj)

if __name__== "__main__":
  main()
