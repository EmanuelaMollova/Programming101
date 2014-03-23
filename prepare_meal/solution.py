def prepare_meal(number):
    numbers = []

    for i in range(1, number):
        if number % 3 ** i == 0:
            numbers.append(i)

    num = max(numbers) if numbers else 0

    if number % 5 == 0 and num != 0:
        eggs = "and eggs"
    elif number % 5 == 0 and num == 0:
        eggs = "eggs"
    else:
        eggs = ""

    return ("spam " * num + eggs).strip()
