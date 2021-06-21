"""
File: largest_digit.py
Name: Claire lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: str, numbers.
	:return: str, the largest digit in this number.
	"""
	number = int(n)
	number_s = str(number)

	if len(number_s) == 1:
		return number_s
	elif len(number_s) == 0:
		return
	else:
		if int(number_s) < 0:
			n *= -1
			number = int(n)
			number_s = str(number)
			return find_largest_digit(number_s)

		elif int(number_s[0]) >= int(number_s[len(number_s)-1]):
			return find_largest_digit(number_s[0:len(number_s)-1])
		else:
			return find_largest_digit(number_s[1:])


if __name__ == '__main__':
	main()
