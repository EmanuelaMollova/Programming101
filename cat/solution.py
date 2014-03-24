import sys


def cat(argv):
    if len(argv) == 2:
        file = open(argv[1], "r")
        content = file.read()
        file.close()

        return content
    else:
        return "There is more than one file or no arguments."


def main():
    print(cat(sys.argv))

if __name__ == '__main__':
    main()
