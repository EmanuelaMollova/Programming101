import sys


def concat_files(argv):
    if len(argv) > 1:
        megatron = open("MEGATRON", "a+")

        content = ""
        for i in range(1, len(argv)):
            file = open(argv[i], "r")
            content += file.read() + "\n"
            file.close()

        megatron.write(content)
        megatron.close()

        return content
    else:
        return "Please give at least one filename."


def main():
    print(concat_files(sys.argv))

if __name__ == '__main__':
    main()
