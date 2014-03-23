import sys

def main():
    if len(sys.argv) > 1:
        file = open(sys.argv[1], "r")
        numbers = file.read().strip().split(" ")
        file.close()
        print(sum(list(map(int, numbers))))
    else:
        print("Please give a filename.")

if __name__ == '__main__':
    main()
