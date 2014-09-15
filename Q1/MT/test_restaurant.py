__author__ = 'Ciddhi'


from restaurant import *


def testRestaurant():
    nSize = 2
    lGuestQueue = []
    objRestaurant = Restaurant(nSize)
    objGuest1 = Guest('Mary', 3)
    lGuestQueue.append(objGuest1)
    objGuest2 = Guest('John', 2)
    lGuestQueue.append(objGuest2)
    objGuest3 = Guest('Alice', 1)
    lGuestQueue.append(objGuest3)

    while len(lGuestQueue) > 0:
        objFirstGuest = lGuestQueue[0]
        bSeated = objRestaurant.seat(objFirstGuest)
        if bSeated:
            lGuestQueue.pop(0)
        objRestaurant.serve()


def testFancyRestaurant():
    nSize = 2
    lGuestQueue = []
    objRestaurant = FancyRestaurant(nSize)
    objGuest1 = Guest('Mary', 3)
    lGuestQueue.append(objGuest1)
    objGuest2 = Guest('John', 2)
    lGuestQueue.append(objGuest2)
    objGuest3 = Guest('Alice', 1)
    lGuestQueue.append(objGuest3)

    while len(lGuestQueue) > 0:
        objFirstGuest = lGuestQueue[0]
        bSeated = objRestaurant.seat(objFirstGuest)
        if bSeated:
            lGuestQueue.pop(0)
        objRestaurant.serve()


if __name__ == "__main__":
    print('Testing Class Restaurant -')
    testRestaurant()
    print('\nTesting Class FancyRestaurant -')
    testFancyRestaurant()