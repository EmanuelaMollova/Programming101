from time import time
from datetime import datetime
import glob
import decimal

def round2(number):
    return round(decimal.Decimal(number), 2)


def take(orders, input_array):
    if len(input_array) == 3:
        name = input_array[1]
        price = float(input_array[2])
    else:
        return "Invalid command! Try take <name> <price>"

    if name in orders:
        orders[name].append(price)
    else:
        orders[name] = [price]

    return "Taking order from {} for {}".format(name, round2(price))


def orders_to_string(orders):
    orders_array = []
    for key in sorted(orders):
        orders_array.append("{} - {}".format(key, round2(str(sum(orders[key])))))

    return "\n".join(orders_array) or False


def status(orders):
    return orders_to_string(orders) or "There are no orders yet."


def save(orders, time = time()):
    if not orders_to_string(orders):
        return "There are no orders to save."

    timestamp = datetime.fromtimestamp(time).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + timestamp
    file = open(filename, "w")
    file.write(orders_to_string(orders))
    file.close()

    return "Saved the current order to {}".format(filename)

def list_order_files():
    list = []
    for index, file in glob.glob('orders_*'):
        list.append(file)

    return list


def list_orders():
    list = []

    for key in list_order_files():
        list.append("[{}] - {}".format(key, list[key]))

    return "\n".join(list)


def load(last_command, number):
    if last_command != "list":
        print("Use list command before loading")
    else:
        print("Good")


def finish(last_command):
    if last_command == "finish":
        print("Finishing order. Goodbye!")
        return True
    else:
        print("Confirm")
        return False


def invalid_command():
    messages = [
        "Unknown command!",
        "Try one of the following:",
        "take <name> <price>",
        "status",
        "save",
        "list",
        "load <number>",
        "finish",
        "Enter command>"
    ]

    return "\n".join(messages)


def check__for_unsaved_changes():
    pass


def parse_orders_from_file(filename, orders):
    orders = {}
    file = open(filename, "r")

    for line in file:
        order = line.split(" - ")
        orders[order[1]] = [order[2]]

    return orders


def execute_command(input_array, orders, last_command, last_saved_state):
    return {
        'take': take(orders, input_array),
        'status': status(orders),
        'save': save(orders)
    }[input_array[0]]


def main():
    all_commands = ["take", "status", "save", "list", "load", "finish"]

    orders = {}
    last_command = None
    last_saved_state = None

    while True:
        input_array = input("Enter command>").split()
        command = input_array[0]

        if command in all_commands:
            print(execute_command(
                input_array,
                orders,
                last_command,
                last_saved_state)
            )
        else:
            print(invalid_command())

        last_command = command

        # if command == "take":
        #     take(input_array, orders)
        # elif command == "status":
        #     status(orders)
        # elif command == "save":
        #     save(orders)
        # elif command == "list":
        #     list_files = list_orders()
        # elif command == "load":
        #     load(last_command, 1)
        # elif command == "finish":
        #     if finish(last_command):
        #         break
        # else:
        #     print(invalid_command())

if __name__ == '__main__':
    main()
