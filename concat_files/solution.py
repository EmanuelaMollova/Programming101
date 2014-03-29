import sys


def concat_files(argv):
    if len(argv) > 1:
        megatron = open("MEGATRON", "a+")
        position = megatron.tell()
        megatron.seek(0)
        content_megatron = megatron.read()

        content = "" if not content_megatron else "\n\n"

        for i in range(1, len(argv)):
            file = open(argv[i], "r")
            content += file.read() + "\n\n"
            file.close()

        megatron.seek(position)
        megatron.write(content.rstrip())
        megatron.close()

        return True
    else:
        return False


def main():
    if not (concat_files(sys.argv)):
        print("Please give at least one filename.")

if __name__ == '__main__':
    main()
