"""
File: anagram.py
Name: Claire Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variables
dictionary = []


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')

    while True:
        word = input('Find anagram for: ')
        word = word.lower()
        if word == EXIT:
            break
        else:
            find_anagrams(word)


def read_dictionary():
    global dictionary

    with open(FILE, 'r') as f:
        for line in f:
            word_dict = line.strip()
            dictionary.append(word_dict)
    # print(dictionary)


def find_anagrams(s):
    """
    :param s: str, the input which will be arranged.
    :return: str, the total arranged words.
    """
    find_lst, s_lst, result = [], [], []

    read_dictionary()

    for ele in s:
        s_lst.append(ele)

    find_anagrams_helper(s, find_lst, result, s_lst)
    print(str(len(result)) + ' anagram: ' + str(result))


def find_anagrams_helper(s, find_lst, result, s_lst):
    """
    :param s: str, the input which will be arranged.
    :param find_lst: lst, the arranged alpha-word will be store here temporarily.
    :param result: lst, the final arranged word store in this list, and will be printed.
    :param s_lst: lst, for dealing with the repeated alpha-word.
    :return: lst, the arranged words.
    """
    global dictionary

    n = ''
    for word in find_lst:
        n += word

    if len(n) == len(s):
        if n in dictionary and n not in result:   # base case
            print('Found: ' + str(n))
            print('Searching...')
            result.append(n)
    else:

        for i in range(len(s)):   # Thanks to Willie for helping me debug.
            if s[i] not in find_lst or s[i] in s_lst:
                find_lst.append(s[i])
                s_lst.remove(s[i])

                if has_prefix(n):
                    find_anagrams_helper(s, find_lst, result, s_lst)
                find_lst.pop()
                s_lst.append(s[i])


def has_prefix(sub_s):
    """
    :param sub_s: str, the first few words in s.
    :return: bool, True or False.
    """
    global dictionary

    for i in dictionary:
        if i.startswith(sub_s):
            if sub_s in i:
                return True
    return False


if __name__ == '__main__':
    main()
