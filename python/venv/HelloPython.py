#!/usr/bin/env python3

"""
Stanford CS106A Command Line Example
Nick Parlante
See the problem description in main()
to write code there.
"""

import sys
import random

AFFIRMATIONS = [
    'Looking good',
    'All hail',
    'Horray for',
    'Today is the day for',
    'I have a good feeling about',
    'A big round of applause for',
    'Everything is coming up',
]


def print_affirm(name):
    """
    Given name, print a random affirmation for that name.
    """
    affirmation = random.choice(AFFIRMATIONS)
    print(affirmation, name)


def print_hello(name):
    """
    Given name, print 'Hello' with that name.
    """
    print('Hello', name)


def print_n_copies(n, name):
    """
    Given int n and name, print n copies of that name.
    """
    print('Hello', name)

def main():
    """
    This program takes 3 command line arg forms:

    1.
    -affirm *name*

    2.
    -hello *name*

    3.
    -n *number* *name*
    """
    # standard - load "args" list with cmd-line-args
    args = sys.argv[1:]

    # args is a list of the command line argument strings that follow
    # the program.py file.
    # So if the command is: python3 affirm.py aaa bbb ccc
    # The args list  will be:
    #   args == ['aaa', 'bbb', 'ccc']
    # The args are all strings, whatever was typed in the terminal.

    # 1. Check for the -affirm arg pattern:
    #   python3 affirm.py -affirm Bart
    #   e.g. args[0] is '-affirm' and args[1] is 'Bart'
    # Select random affirmation phrase
    # Print with the name in args[1]

    if len(args) == 2 and args[0] == '-affirm':
        affirmation = random.choice(AFFIRMATIONS)
        print(affirmation, args[1])

    # 2 - Check for -hello args pattern:
    #   python3 affirm.py -hello Lisa
    # Print out: Hello Lisa
    # Here 'Hello' is fixed, nothing random.

    pass


    # 3 - Check for -n args pattern:
    #   python3 affirm.py -n 100 Maggie
    # Print out 100 copies of 'Maggie' separated by spaces
    # Note: the command line arg is a string, convert to int

    pass


# Python boilerplate.
if __name__ == '__main__':
    main()
