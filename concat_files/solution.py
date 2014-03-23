import sys

def main():
    if len(sys.argv) > 1:
        megatron = open("MEGATRON", "a+")

        content = ""
        for i in range(1, len(sys.argv)):
            file = open(sys.argv[i], "r")
            content += file.read() + "\n"
            file.close()
        megatron.write(content)
        megatron.close()
    else:
        print("Please give at least one filename.")

if __name__ == '__main__':
    main()
