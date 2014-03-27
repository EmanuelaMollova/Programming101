import sys


def wc(argv):
    if len(argv) > 2:
        commands = ["chars", "words", "lines"]

        command = argv[1]
        if command in commands:
            file = open(argv[2], "r")

            if command == "chars":
                contents = list(file.read())
            elif command == "words":
                contents = file.read().split()
            elif command == "lines":
                contents = file.read().split("\n")

            file.close()

            return len(contents)
        else:
            return "The given command is not valid"
    else:
        return "Please give a command and a filename."


def main():
    print(wc(sys.argv))

if __name__ == '__main__':
    main()
