import sys


def cat2(argv):
    if len(argv) > 1:
        content = ''
        for i in range(1, len(argv)):
            file = open(argv[i], "r")
            content += file.read() + "\n"
            file.close()

        return content.strip()
    else:
        return "There are no arguments."


def main():
    print(cat2(sys.argv))

if __name__ == '__main__':
    main()
