"""
File: boggle.py
Name: Claire Lin
----------------------------------------
TODO: Build the boggle game!
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
dictionary = []


def main():
	"""
	TODO: User need to input 4 words in each 4 rows, then the program will output the answer.
	"""
	print('Please input 4 words in the next 4 rows. (ex. a b c d)')

	row_list = []
	count = 1

	for i in range(4):
		row_input = []

		row = input(str(count) + ' row of letters: ')
		row = row.lower()
		if len(row) != 7 or row[1].isalpha() or row[3].isalpha() or row[5].isalpha():
			print('illegal format')
			break
		elif row[0].isalpha() or row[2].isalpha() or row[4].isalpha() or row[6].isalpha():
			row_input += row[0]
			row_input += row[2]
			row_input += row[4]
			row_input += row[6]
			count += 1
			row_list.append(row_input)

	if len(row_list) == 4:
		# print(row_list)
		find_word(row_list)


def find_word(word_list):
	"""
	:param word_list: str, the input words.
	:return: str, the results.
	"""
	read_dictionary()

	result = []

	for x in range(4):
		for y in range(4):
			first_word = str(word_list[x][y])
			chosen_list = [(x, y)]
			find_word_helper(word_list, first_word, x, y, chosen_list, result)

	print('There are ' + str(len(result)) + ' words in total.')


def find_word_helper(lst, word, x, y, chosen_list, result):
	"""
	:param lst: list, the input words.
	:param word: str, the first word to run.
	:param x: int, the index of each rows.
	:param y: int, the index of alpha-word in each rows.
	:param chosen_list: list, after the alpha-word been picked, mark the chosen site.
	:param result: list, record the words been found.
	:return: chosen list and result.
	"""
	global dictionary

	if len(word) >= 4 and word in dictionary and word not in result:   # base case
		print('Found \"' + str(word) + '\"')
		result.append(word)
		find_word_helper(lst, word, x, y, chosen_list, result)  # for the word been founded, can be keep searching more.

	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= (x+i) < 4 and 0 <= (y+j) < 4:
					if (x+i, y+j) not in chosen_list:
						alpha = lst[x+i][y+j]   # Choose
						word += alpha

						chosen_site = (x+i, y+j)
						chosen_list.append(chosen_site)   # Mark the chosen_site.

						if has_prefix(word):   # Explore
							find_word_helper(lst, word, x+i, y+j, chosen_list, result)

						word = word[:len(word)-1]   # Un-choose
						chosen_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary

	with open(FILE, 'r') as f:
		for line in f:
			word_dict = line.strip()
			dictionary.append(word_dict)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global dictionary

	for i in dictionary:
		if i.startswith(sub_s):
			if sub_s in i:
				return True
	return False


if __name__ == '__main__':
	main()
