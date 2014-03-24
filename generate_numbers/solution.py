import sys
from random import randint


def get_n_random_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(str(randint(1, 1000)))

    return numbers


def generate_numbers(argv):
    if len(argv) > 2:
        numbers_count = int(argv[2])
        content = " ".join(get_n_random_numbers(numbers_count))

        file = open(argv[1], "w")
        file.write(content)
        file.close()

        return content
    else:
        return("Please give a filename and a number.")


def main():
    print(generate_numbers(sys.argv))

if __name__ == '__main__':
    main()
