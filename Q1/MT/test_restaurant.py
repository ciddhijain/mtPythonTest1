__author__ = 'Ciddhi'


from restaurant import *

# function to seat and serve a guest in Restaurant alternatively
def testRestaurant():
    nSize = 2
    lGuestQueue = []            # waiting guest queue
    objRestaurant = Restaurant(nSize)
    objGuest1 = Guest('Mary', 3)
    lGuestQueue.append(objGuest1)
    objGuest2 = Guest('John', 2)
    lGuestQueue.append(objGuest2)
    objGuest3 = Guest('Alice', 1)
    lGuestQueue.append(objGuest3)

    # iterate till there are guests waiting to be seated, seat and serve alternatively
    while len(lGuestQueue) > 0:
        objFirstGuest = lGuestQueue[0]
        bSeated = objRestaurant.seat(objFirstGuest)

        # pop guest out of queue once he/she is seated
        if bSeated:
            lGuestQueue.pop(0)
        objRestaurant.serve()


# function to seat and serve a guest in fancyRestaurant alternatively
def testFancyRestaurant():
    nSize = 2
    lGuestQueue = []            # waiting guest queue
    objRestaurant = FancyRestaurant(nSize)
    objGuest1 = Guest('Mary', 3)
    lGuestQueue.append(objGuest1)
    objGuest2 = Guest('John', 2)
    lGuestQueue.append(objGuest2)
    objGuest3 = Guest('Alice', 1)
    lGuestQueue.append(objGuest3)

    # iterate till there are guests waiting to be seated, seat and serve alternatively
    while len(lGuestQueue) > 0:
        objFirstGuest = lGuestQueue[0]
        bSeated = objRestaurant.seat(objFirstGuest)

        # pop guest out of queue once he/she is seated
        if bSeated:
            lGuestQueue.pop(0)
        objRestaurant.serve()


if __name__ == "__main__":
    print('Testing Class Restaurant -')
    testRestaurant()
    print('\nTesting Class FancyRestaurant -')
    testFancyRestaurant()