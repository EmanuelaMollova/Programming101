import sys


def sum_numbers(argv):
    if len(argv) > 1:
        file = open(argv[1], "r")
        numbers = file.read().strip().split(" ")
        file.close()

        return sum(list(map(int, numbers)))
    else:
        return "Please give a filename."


def main():
    print(sum_numbers(sys.argv))

if __name__ == '__main__':
    main()
