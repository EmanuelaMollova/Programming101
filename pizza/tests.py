import unittest
from time import time
from datetime import datetime
import os
import pizza


class PizzaTest(unittest.TestCase):
    def setUp(self):
        self.last_saved_state = None

        self.orders = {
            'Emi': [10.00],
            'Ivo': [5.00, 20.00]
        }

        self.orders2 = {
            'Jane': [15.00, 0.50],
            'Jack': [5.00]
        }

        expected = [
            'Emi - 10.00',
            'Ivo - 25.00'
        ]

        self.expected_string = "\n".join(expected)

        timestamp = datetime.fromtimestamp(time()).strftime('%Y_%m_%d_%H_%M_%S')
        self.filename = "orders_" + timestamp

        time2 = time() + 60
        timestamp2 = datetime.fromtimestamp(time2).strftime('%Y_%m_%d_%H_%M_%S')
        self.filename2 = "orders_" + timestamp2

        self.assertTrue(
            "Saved the current order to {}.".format(timestamp),
            pizza.save(self.orders, self.last_saved_state)
        )
        pizza.save(self.orders2, self.last_saved_state, time2)

        self.file = open(self.filename, 'r')
        self.file2 = open(self.filename2, 'r')

    def test_take_expects_two_parameters(self):
        error_message = "Invalid command! Try take <name> <price>"
        self.assertEqual(error_message, pizza.take(self.orders, ['take']))
        self.assertEqual(error_message, pizza.take(self.orders, []))

    def test_take_adds_new_orders(self):
        message = "Taking order from {} for {}"
        self.assertEqual(message.format('John', '10.50'), pizza.take(self.orders, ['take', 'John', '10.5']))
        self.assertEqual(3, len(self.orders))
        self.assertEqual(1, len(self.orders['John']))
        self.assertEqual(10.5, self.orders['John'][0])

    def test_take_adds_orders_to_existing_person(self):
        message = "Taking order from {} for {}"
        self.assertEqual(message.format('Emi', '2.00'), pizza.take(self.orders, ['take', 'Emi', '2']))
        self.assertEqual(2, len(self.orders))
        self.assertEqual(2, len(self.orders['Emi']))
        self.assertEqual(2.00, self.orders['Emi'][1])
        self.assertEqual(12.00, sum(self.orders['Emi']))

    def test_orders_to_string_works_with_orders(self):
        self.assertEqual(self.expected_string, pizza.orders_to_string(self.orders))

    def test_orders_to_string_works_without_orders(self):
        self.assertTrue(not pizza.orders_to_string({}))

    def test_status_works_without_orders(self):
        self.assertTrue("There are no orders yet.", pizza.status({}))

    def test_save_works_without_orders(self):
        self.assertTrue("There are no orders to save.", pizza.save({}, self.last_saved_state))

    def test_save_works_with_orders(self):
        content = self.file.read()
        self.assertEqual(self.expected_string, content)

    def test_list_order_files(self):
        self.assertEqual(2, len(pizza.list_order_files()))
        self.assertEqual(self.filename, pizza.list_order_files()[0])

    def test_list_orders(self):
        self.assertEqual("[1] - {}\n[2] - {}".format(self.filename, self.filename2), pizza.list_orders())

    def test_load_needs_the_last_command_to_be_list(self):
        self.assertEqual("Use list command before loading", pizza.load('status', 2, self.last_saved_state, self.orders))

    def test_load_reminds_to_save_orders(self):
        expected_string = "You have not saved the current order.\nIf you wish to discard it, type load <number> again."
        self.assertEqual(expected_string, pizza.load('list', 2, {}, self.orders))

    def tearDown(self):
        self.file.close()
        os.remove(self.filename)
        os.remove(self.filename2)

if __name__ == '__main__':
    unittest.main()
