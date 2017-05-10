#!/usr/bin/env python

import sys

def main():
    negative = 0
    positve = 0
    with file(sys.argv[1]) as f:
        for line in f:
            if line.split()[1] == '1':
                positve += 1
            else:
                negative += 1
    print "positive / negative: " + str(positve) + ' / ' + str(negative)
    sumAll = positve + negative
    print "all: " + str(sumAll)

if __name__ == "__main__":
    main()
