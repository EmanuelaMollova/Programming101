import unittest
import pizza


class PizzaTest(unittest.TestCase):
    def setUp(self):
        self.orders = {
            'Emi': [10.00],
            'Ivo': [5.00, 20.00]
        }

    def test_take_expects_two_parameters(self):
        error_message = "Invalid command! Try take <name> <price>"
        self.assertEqual(error_message, pizza.take(self.orders, ['take']))
        self.assertEqual(error_message, pizza.take(self.orders, []))

    def test_take_adds_new_orders(self):
        message = "Taking order from {} for {}"
        self.assertEqual(message.format('Rado', '10.5'), pizza.take(self.orders, ['take', 'Rado', '10.5']))
        self.assertEqual(3, len(self.orders))
        self.assertEqual(1, len(self.orders['Rado']))
        self.assertEqual(10.5, self.orders['Rado'][0])

    def test_take_adds_orders_to_existing_person(self):
        message = "Taking order from {} for {}"
        self.assertEqual(message.format('Emi', '2.0'), pizza.take(self.orders, ['take', 'Emi', '2']))
        self.assertEqual(2, len(self.orders))
        self.assertEqual(2, len(self.orders['Emi']))
        self.assertEqual(2.00, self.orders['Emi'][1])
        self.assertEqual(12.00, sum(self.orders['Emi']))

if __name__ == '__main__':
    unittest.main()
