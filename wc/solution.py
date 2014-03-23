import sys

def main():
    if len(sys.argv) > 2:
        commands = ["chars", "words", "lines"]

        command = sys.argv[1]
        if command in commands:
            file = open(sys.argv[2], "r")

            if command == "chars":
                contents = list(file.read())
            elif command == "words":
                contents = file.read().split()
            elif command == "lines":
                contents = file.read().split("\n")

            print(len(contents))
        else:
            print ("The given command is not valid")
    else:
        print("Please give a command and a filename.")

if __name__ == '__main__':
    main()
