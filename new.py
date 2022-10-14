#!/usr/bin/env python3
""" Add here some title """

import argparse
from typing import NamedTuple

class Args(NamedTuple):
    """ Command-line arguments """
    dna : str

# ---------------------------------------------------------

def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    return parser.parse_args()

# ---------------------------------------------------------

def main():
    """ Make a jazz noise here """

    args = get_args()
    print(args.dna / 2)

# ---------------------------------------------------------

if __name__ == '__main__':
    main()