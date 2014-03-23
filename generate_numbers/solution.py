import sys
from random import randint

def main():
    if len(sys.argv) > 2:
        numbers_count = int(sys.argv[2])
        content = ""
        # separate in function ?
        for i in range (0, numbers_count):
            content += str(randint(1, 1000)) + " "
        filename = sys.argv[1]
        file = open(filename, "w")
        file.write(content.strip())
        file.close()
    else:
        print("Please give a filename and a number.")

if __name__ == '__main__':
    main()
