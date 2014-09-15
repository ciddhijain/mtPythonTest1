__author__ = 'Ciddhi'


# Base class to define comparison operators.
# modulus 3 operation is used to implement circularity
class Gesture(object):

    def __init__(self, index=0):
        self.index = index

    # functionality for less than or equal to
    def __le__(self, other):
        nDiff = self.index - other.index

        # when both are same
        if nDiff%3 == 0:
            return True

        # when first is lesser than second
        if nDiff%3 == 1:
            return True

        # when first is greater than second
        if nDiff%3 == 2:
            return False

    # functionality for greater than or equal to
    def __ge__(self, other):
        nDiff = self.index - other.index

        # when both are same
        if nDiff%3 == 0:
            return True

        # when first is lesser than second
        if nDiff%3 == 1:
            return False

        # when first is greater than second
        if nDiff%3 == 2:
            return True

    def __lt__(self, other):
        nDiff = self.index - other.index

        # when both are same
        if nDiff%3 == 0:
            return False

        # when first is lesser than second
        if nDiff%3 == 1:
            return True

        # when first is greater than second
        if nDiff%3 == 2:
            return False

    def __gt__(self, other):
        nDiff = self.index - other.index

        # when both are same
        if nDiff%3 == 0:
            return False

        # when first is lesser than second
        if nDiff%3 == 1:
            return False

        # when first is greater than second
        if nDiff%3 == 2:
            return True

    def __eq__(self, other):
        nDiff = self.index - other.index

        # when both are same
        if nDiff%3 == 0:
            return True

        # when first is lesser than second
        if nDiff%3 == 1:
            return False

        # when first is greater than second
        if nDiff%3 == 2:
            return False

class Rock(Gesture):

    # initilize with index 1
    def __init__(self):
        return super(Rock, self).__init__(1)

    def __str__(self):
        return 'Rock'


class Scissor(Gesture):

    # initilize with index 2
    def __init__(self):
        return super(Scissor, self).__init__(2)

    def __str__(self):
        return 'Scissor'


class Paper(Gesture):

    # initilize with index 3
    def __init__(self):
        return super(Paper, self).__init__(3)

    def __str__(self):
        return 'Paper'