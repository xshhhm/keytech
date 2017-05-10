import sys

def main():
    num = 0
    infile = file(sys.argv[1])
    for line in infile:
        line = line.strip()
        datasplit = line.split(" ")
        print datasplit[0], datasplit[1]
        num += 1
    infile.close()
    
    print num

if __name__ == "__main__":
    main()
