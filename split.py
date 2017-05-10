#!/usr/bin/env python
import random
import sys

def remove_chances(p):
    return 1.0 - (1.0 - p) / p;

def main():

    infile = file(sys.argv[1])
    train_name = sys.argv[1] + "_train"
    val_name = sys.argv[1] + "_val"
    outfile_train = file(train_name, 'w')
    outfile_val = file(val_name, 'w')

    try:
        cutdownto = float(sys.argv[2])
    except IndexError:
        print "cutdown to ... NOT PROVIDED, use 0.1 as default"
        cutdownto = 0.9

    trainNum = 0
    validationNum = 0
    
    for line in infile:
        if random.random() < cutdownto:
            outfile_train.write(line)
            trainNum += 1
        else:
            outfile_val.write(line)
            validationNum += 1
            
                

    infile.close()
    outfile_train.close()
    outfile_val.close()

    print "cutdownto: " + str(cutdownto)

    print "train / val: " + str(trainNum) + ' / ' + str(validationNum)
    sumAll = trainNum + validationNum
    print "all: " + str(sumAll)
    
if __name__ == "__main__":
    main()
