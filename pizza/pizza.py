from time import time
from datetime import datetime
import glob


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

    return "Taking order from {} for {}".format(name, price)


def orders_to_string(orders):
    orders_array = []
    for key in orders:
        orders_array.append("{} - {}".format(key, str(sum(orders[key]))))

    return "\n".join(orders_array)


def status(orders):
    return orders_to_string(orders)


def save(orders):
    timestamp = datetime.fromtimestamp(time()).strftime('%Y_%m_%d_%H_%M_%S')

    filename = "orders_" + timestamp
    file = open(filename, "w")
    file.write(orders_to_string(orders))
    file.close()

    return "Saved the current order to {}".format(filename)


def list_orders():
    i = 1
    list = {}
    for file in glob.glob('orders_*'):
        list[i] = file
        i += 1

    for key in list:
        print("[%s] %s" % (key, list[key]))

    return list

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


def main():
    all_commands = ["take", "status", "save", "list", "load", "finish"]


    last_command = ''
    orders = {}

# def execute_command(all_commands, function_name, arg):
#     possibles = globals().copy()
#     possibles.update(locals())
#     function = possibles.get(function_name)
#     if function_name in all_commands:
#         return function(arg) if arg else function()
#     else:
#         return "Please select valid command."


# def main():
#     all_commands = [
#         "list_employees",
#         "monthly_spending",
#         "yearly_spending",
#         "add_employee",
#         "delete_employee",
#         "update_employee"
#     ]

#     while True:
#         command = input("command>").split()
#         arg = None if len(command) == 1 else command[1]

#         print(execute_command(all_commands, command[0], arg))
    while True:
        input_array = input("Enter command>").split()
        command = input_array[0]
        called_commands.append(command)

        # if command in all_commands:
        #     command.call()

        if command == "take":
            take(input_array, orders)
        elif command == "status":
            status(orders)
        elif command == "save":
            save(orders)
        elif command == "list":
            list_files = list_orders()
        elif command == "load":
            load(last_command, 1)
        elif command == "finish":
            if finish(last_command):
                break
        else:
            print(invalid_command())

if __name__ == '__main__':
    main()
