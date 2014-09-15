__author__ = 'Ciddhi'

import unittest
from restaurant import *


# To test class Restaurant
class testRestaurant(unittest.TestCase):

    # To test case when first guest arrives
    def test_seat_mary(self):
        print('\nRestaurant : Test seating Mary - ')
        self.assertEqual(Restaurant(2).seat(Guest('Mary', 3)), True)

    # To test case when there is no space available
    def test_seat_john(self):
        print('\nRestaurant : Test seating John - ')
        objRestaurant = Restaurant(1)
        objRestaurant.seat(Guest('Mary', 2))
        self.assertEqual(objRestaurant.seat(Guest('John', 2)), False)

    # To test when some hungry guest is served
    def test_serve_mary(self):
        print('\nRestaurant : Test serving Mary - ')
        objRestaurant = Restaurant(1)
        objRestaurant.seat(Guest('Mary', 1))
        self.assertEqual(objRestaurant.serve(), True)

    # To test case when some guests wants no more to eat
    def test_serve_john(self):
        print('\nRestaurant : Test serving John - ')
        objRestaurant = Restaurant(1)
        objRestaurant.seat(Guest('John', 2))
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), False)

    # To test case when some person leaves and space becomes available
    def test_seat_alice(self):
        print('\nRestaurant : Test seating Alice - ')
        objRestaurant = Restaurant(2)
        objRestaurant.seat(Guest('Mary',1))
        objRestaurant.seat(Guest('John', 1))
        self.assertEqual(objRestaurant.seat(Guest('Alice', 2)), False)
        objRestaurant.serve()
        self.assertEqual(objRestaurant.seat(Guest('Alice', 2)), True)


# To test class FancyRestaurant
class testFancyRestaurant(unittest.TestCase):

    # To test case when a guest is served
    def test_serve_mary(self):
        print('\nFancyRestaurant : Test serving Mary - ')
        objRestaurant = FancyRestaurant(1)
        objRestaurant.seat(Guest('Mary', 2))
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), False)

    # To test case when multiple guests are served one-by-one
    def test_serve_alice(self):
        print('\nFancyRestaurant : Test serving Alice - ')
        objRestaurant = FancyRestaurant(2)
        objRestaurant.seat(Guest('Mary',2))
        objRestaurant.seat(Guest('John', 2))
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), False)
        objRestaurant.seat(Guest('Alice',2))
        self.assertEqual(objRestaurant.serve(), True)
        self.assertEqual(objRestaurant.serve(), False)


if __name__ == '__main__':
    unittest.main()
