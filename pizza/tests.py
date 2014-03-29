import unittest
from time import time
from datetime import datetime
import os
import pizza


class PizzaTest(unittest.TestCase):
    def setUp(self):
        self.orders = {
            'Emi': [10.00],
            'Ivo': [5.00, 20.00]
        }

        expected = [
            'Emi - 10.00',
            'Ivo - 25.00'
        ]

        self.expected_string = "\n".join(expected)

    def test_take_expects_two_parameters(self):
        error_message = "Invalid command! Try take <name> <price>"
        self.assertEqual(error_message, pizza.take(self.orders, ['take']))
        self.assertEqual(error_message, pizza.take(self.orders, []))

    def test_take_adds_new_orders(self):
        message = "Taking order from {} for {}"
        self.assertEqual(message.format('Rado', '10.50'), pizza.take(self.orders, ['take', 'Rado', '10.5']))
        self.assertEqual(3, len(self.orders))
        self.assertEqual(1, len(self.orders['Rado']))
        self.assertEqual(10.5, self.orders['Rado'][0])

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
        self.assertTrue("There are no orders to save.", pizza.save({}))

    def test_save_works_with_orders(self):
        timestamp = datetime.fromtimestamp(time()).strftime('%Y_%m_%d_%H_%M_%S')

        self.assertTrue(
            "Saved the current order to {}.".format(timestamp),
            pizza.save(self.orders)
        )

        file = open("orders_" + timestamp, 'r')
        content = file.read()
        file.close()

        self.assertEqual(self.expected_string, content)

        os.remove("orders_" + timestamp)

if __name__ == '__main__':
    unittest.main()
