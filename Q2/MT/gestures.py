__author__ = 'Ciddhi'

class Gesture(object):

    def __init__(self, index=0):
        self.index = index

    def __le__(self, other):
        nDiff = self.index - other.index
        if nDiff%3 == 0:
            return True
        if nDiff%3 == 1:
            return True
        if nDiff%3 == 2:
            return False

    def __ge__(self, other):
        nDiff = self.index - other.index
        if nDiff%3 == 0:
            return True
        if nDiff%3 == 1:
            return False
        if nDiff%3 == 2:
            return True

    def __lt__(self, other):
        nDiff = self.index - other.index
        if nDiff%3 == 0:
            return False
        if nDiff%3 == 1:
            return True
        if nDiff%3 == 2:
            return False

    def __gt__(self, other):
        nDiff = self.index - other.index
        if nDiff%3 == 0:
            return False
        if nDiff%3 == 1:
            return False
        if nDiff%3 == 2:
            return True

    def __eq__(self, other):
        nDiff = self.index - other.index
        if nDiff%3 == 0:
            return True
        if nDiff%3 == 1:
            return False
        if nDiff%3 == 2:
            return False

class Rock(Gesture):

    def __init__(self):
        return super(Rock, self).__init__(1)


class Scissor(Gesture):

    def __init__(self):
        return super(Scissor, self).__init__(2)


class Paper(Gesture):

    def __init__(self):
        return super(Paper, self).__init__(3)

'''
r = Rock()
s = Scissor()
p = Paper()
print('Rock is same as Scissor : ' + str(r==s))
print('Rock is greater than Scissor : ' + str(r>s))
print('Paper is greater than Rock : ' + str(p>r))
print('Scissor is lesser than Paper : ' + str(s<p))
'''