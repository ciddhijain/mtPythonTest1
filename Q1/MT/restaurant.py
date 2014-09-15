__author__ = 'Ciddhi'


# Class defining properties and functions of a guest
class Guest:

    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1
            return True
        else:
            print(self.name + ': Burp')
            return False


# Class defining properties and functions of a basic restaurant
class Restaurant(list):

    # function to initialize a list of given size
    def __init__(self, size=0):
        self.size = size
        for i in range(size):
            self.append(None)

    # function to seat an incoming guest if space is available
    def seat(self, guest):
        seated = False

        # iterate through all seats and check if atleast one is empty
        for i in range(self.size):
            if self.__getitem__(i) is None:
                self.__setitem__(i,guest)
                seated = True
                print('Seating guest ' + guest.name + ' at table ' + str(i) + '.')
                break

        # Check if guest has been seated on some empty table
        if not seated:
            print('No free Table')
            return False

        return True

    # function to serve a guest. It serves one unit to one guest at a time
    def serve(self):
        served = False

        # iterate through all seats and check if some guest is hungry.
        for i in range(self.size):
            guest = self.__getitem__(i)
            if guest is not None:

                # If hunger is greater than 1 unit, let him sit further. Else, vacate the seat after feeding him
                if guest.hunger > 1:
                    print('Serving guest ' + guest.name + '.')
                    guest.eat()
                elif guest.hunger>0:
                    print('Serving guest ' + guest.name + '.')
                    guest.eat()
                    print(guest.name + ': Burp !')
                    self.__setitem__(i,None)
                served = True
                break

        # Check if there was some guest to serve
        if not served:
            print('No guest to serve')
            return False
        return True


# Class defining properties and functions of an advanced restaurant
class FancyRestaurant(Restaurant):

    # Overloading function serve from base class
    # Function to serve a guest as much as he/she wants at a time.
    def serve(self):
        served = False

        # iterate through all seats to find a hungry guest. Feed him and vacate the seat afterwards
        for i in range(self.size):
            guest = self.__getitem__(i)
            if guest is not None:
                print('Serving guest ' + guest.name + '.')
                for j in range(guest.hunger):
                    guest.eat()
                    if guest.hunger == 0:
                        print(guest.name + ': Burp !')
                        self.__setitem__(i, None)
                served = True
                break

        # Check if there was some guest to serve
        if not served:
            print('No guest to serve')
            return False

        return True