"""
File: similarity.py
Name:Claire Lin
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO: To find the best match of DNA similarity.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')

    best_match = find_match(short_sequence, long_sequence)
    print('The best match is '+str(best_match))


def find_match(short_sequence, long_sequence):
    """
    :param short_sequence: str, the one we want to align in long-sequence.
    :param long_sequence: str, the original sequence.
    :return: str, find the short-sequence's best match in long-sequence.
    """
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    rate = 0
    new_seq = ''
    biggest_rate = 0

    # Willie taught me to set the limit of range.
    for i in range(len(long_sequence)-len(short_sequence)+1):
        rate = 0
        for j in range(i, i+len(short_sequence)):

            if long_sequence[j] == short_sequence[(j-i)]:
                rate += 20
            else:
                rate += 0

        if rate >= biggest_rate:
            biggest_rate = rate
            new_seq = long_sequence[i:i + len(short_sequence)]
    return new_seq























###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
