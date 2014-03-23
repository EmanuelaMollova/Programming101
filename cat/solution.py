import sys


def cat_helper(argv):
    if len(argv) > 1:
        file = open(argv[1], "r")
        content = file.read()
        file.close()

        return content
    else:
        return "There are no arguments"


def main():
    print(cat_helper(sys.argv))

if __name__ == '__main__':
    main()
