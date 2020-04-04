# - - - - - - - - - - - - - - - - - - - - - - -
# CIS 315 Spring 2020
# Intermediate Algorithms
#
# Assignment 0: Write a program which will
# read a series of pairs of integers X & Y
# and print pairs X + Y & X * Y.
#
# Author: Nathan Malamud
# - - - - - - - - - - - - - - - - - - - - - - -

import sys

def main():
    """ Program Driver """

    # print("Num args:", len(sys.argv))

    if len(sys.argv) >= 2:
        print("Invalid use. Input must be given through stdin, not argv.")
        exit(1)

    else:
        f_in = sys.stdin
        f_out = sys.stdout

	# - - - N := how many lines will follow. - - - #
        N = int(f_in.readline())

        for i in range(N):
            numList = f_in.readline().split(' ')
            X = int(numList[0])
            Y = int(numList[1])
            f_out.write(f"{(lambda x, y: x + y)(X, Y)}" + ' ' +
                        f"{(lambda x, y: x * y)(X, Y)}" + '\n')

        exit(0)


if __name__ == "__main__":
    main()
