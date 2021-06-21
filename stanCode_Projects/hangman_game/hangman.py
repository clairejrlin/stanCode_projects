"""
File: hangman.py
Name:Claire Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: The game runs the word in random, users need to guess it and save hang man's life.
    (But after program jump out from the illegal format, life still loose one even guess right XD)
    """
    play_game()


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def play_game():
    """
    Input string, program will distinguish the word in answer.
    :return: string, if users guess right, the string will record the answer down till they win.
                     when users guess wrong, hang man's life will be less.
    (...after program jump out from the illegal format, life still loose one even guess right, sorry XD)
    """
    word = random_word()
    life = N_TURNS
    ans = ''

    old_s = '-' * len(word)

    while True:
        print('The word looks like: ' + str(old_s))
        print('You have ' + str(life) + ' guesses left.')

        # To print the platform picture.
        if life == N_TURNS:
            print('---------------', end='')
            print('')
            for i in range(5):
                for j in range(1):
                    print(' |')
            print('---')

        guess = input('Your guess: ')
        guess = guess.upper()

        # To default the illegal format, but still loose life even guess correct @@.
        while not guess.isalpha() or not len(guess) == 1:
            print('\"illegal format\"')
            guess = input('Your guess: ')

        # The game starts.
        if guess not in word:
            life += -1
            print('There is no ' + str(guess) + '\'s' ' in the word.')

            hang_man(life)  # draw hang man images when life decreased.

            if life == 0:
                print('---------------', end='')
                print('')
                print(' |     ^|^     ')
                print(' |   (_X Xo)   ')
                print(' |    / U \\   ')
                print(' |   /  || \\  ')
                print(' |     /  \\   ')
                print(' |    /    \\  ')
                print('---')
                print('You are completely hung :(')
                print('The word was: ' + str(word))
                break

        else:
            ans = ''
            if guess in word:
                print('You are correct!')
                i = word.find(guess)
                w = word[i]
                for i in range(len(word)):
                    if guess == word[i]:
                        ans += w
                    else:
                        ans += old_s[i]
                old_s = ans  # To store the answer.

        if ans == word:
            print('')
            print(' *    ^ ^   *  YA!')
            print('  \\ (_^ ^_) /    ')
            print('       ||   *     ')
            print('   *   ||       * ')
            print('      /  \\/      ')
            print(' *   /         *  ')
            print('You win !!')
            print('The word was ' + str(word))
            break


def hang_man(life):
    """
    :param life: int, from constant number N_TURNS.
    :return: string, showing the danger happening on hang man, he's nervous.
    """

    if life == N_TURNS - 1:
        print('---------------', end='')
        print('')
        print(' |      |    ')
        print(' |     ^|^   ')
        print(' |   (_O O_) ')
        for i in range(4):
            for j in range(1):
                print(' |')
        print('---')

    elif life == N_TURNS - 2:
        print('---------------', end='')
        print('')
        print(' |      |     ')
        print(' |     ^|^    ')
        print(' |   (_O O_)  ')
        print(' |      ||    ')
        print(' |      ||    ')
        for i in range(2):
            for j in range(1):
                print(' |')
        print('---')

    elif life == N_TURNS - 3:
        print('---------------', end='')
        print('')
        print(' |      |     ')
        print(' |     ^|^    ')
        print(' |   (_O O_)  ')
        print(' |    / ||    ')
        print(' |   /  ||    ')
        for i in range(2):
            for j in range(1):
                print(' |')
        print('---')

    elif life == N_TURNS - 4:
        print('---------------', end='')
        print('')
        print(' |      |       ')
        print(' |     ^|^      ')
        print(' |   (_O O_)    ')
        print(' |    / ||\\    ')
        print(' |   /  || \\   ')
        for i in range(2):
            for j in range(1):
                print(' |')
        print('---')

    elif life == N_TURNS - 5:
        print('---------------', end='')
        print('')
        print(' |      |       ')
        print(' |     ^|^      ')
        print(' |   (_Q Q\")   ')
        print(' |    / ||\\    ')
        print(' |   /  || \\   ')
        print(' |     /        ')
        print(' |    /         ')
        print('---')

    elif life == N_TURNS - 6:
        print('---------------', end='')
        print('')
        print(' |      |       ')
        print(' |     ^|^      ')
        print(' |   ( QAQ\")   ')
        print(' |    / ||\\    ')
        print(' |   /  || \\   ')
        print(' |     /  \\    ')
        print(' |    /    \\   ')
        print('---')


"""
Second try...
I put A to Z separately.
"""
# if guess in word and guess == 'A':
#     print('You are correct!')
#     i = word.find(guess)
#     w = word[i]
#     for i in range(len(word)):
#         if guess == word[i]:
#             ans += w
#         else:
#             ans += old_s[i]
#     old_s = ans
# elif guess in word and guess == 'B':
#     print('You are correct!')
#     i = word.find(guess)
#     w = word[i]
#     for i in range(len(word)):
#         if guess == word[i]:
#             ans += w
#         else:
#             ans += old_s[i]
#     old_s = ans
#     .................


"""
First try ...
First style of program, but the fault is if the random word change, the program can't run smoothly.
"""

# def play_game():
#     word = random_word()
#     life = N_TURNS
#     ans = ''
#
#     if word == 'NOTORIOUS':
#         old_s = '---------'
#         while True:
#             print('The word looks like: '+str(old_s))
#             print('You have ' + str(life) + ' guesses left.')
#             guess = input('Your guess: ')
#             guess = guess.upper()
#
#             if not guess.isalpha() or len(guess) > 1:
#                 print('illegal format')
#
#             elif guess not in 'NOTORIOUS':
#                 life += -1
#                 print('There is no '+str(guess)+'\'s' ' in the word.')
#
#                 if life == 0:
#                     print('You are completely hung :(')
#                     print('The word was: '+str(word))
#                     break
#
#             else:
#                 ans = ''
#                 if guess in 'NOTORIOUS' and guess == 'N':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += w
#                     ans += old_s[1:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'O':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0]
#                     ans += w
#                     ans += old_s[2]
#                     ans += w
#                     ans += old_s[4:6]
#                     ans += w
#                     ans += old_s[7:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'T':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0:2]
#                     ans += w
#                     ans += old_s[3:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'R':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0:4]
#                     ans += w
#                     ans += old_s[5:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'I':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0:5]
#                     ans += w
#                     ans += old_s[6:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'U':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0:7]
#                     ans += w
#                     ans += old_s[8:]
#                     old_s = ans
#
#                 elif guess in 'NOTORIOUS' and guess == 'S':
#                     print('You are correct!')
#                     i = word.find(guess)
#                     w = word[i]
#                     ans += old_s[0:8]
#                     ans += w
#                     old_s = ans
#
#             if ans == 'NOTORIOUS':
#                 print('You win !!')
#                 print('The word was '+str(word))
#                 break
#       .................


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
