"""
File: rocket.py
Name:Claire Lin
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	:return: str, the rocket will be build in any size.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):
		print(' ', end='')
		for j in range(-i+(SIZE-1)):
			print(' ', end='')
		for k in range(i+1):
			print('/', end='')
		for l in range(i+1):
			print('\\', end='')
		print("")


def belt():
	print('+', end='')
	for k in range(SIZE*2):
		print('=', end='')
	print('+')


def upper():
	for m in range(SIZE):
		print('|', end='')
		for n in range(-m+(SIZE-1)):
			print('.', end='')
		for u in range(m+1):
			print('/\\', end='')
		for s in range(-m+(SIZE - 1)):
			print('.', end='')
		print('|')


def lower():
	for o in range(SIZE):
		print('|', end='')
		for p in range(o):
			print('.', end='')
		for r in range(-o+SIZE):
			print('\\/', end='')
		for q in range(o):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()