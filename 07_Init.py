'''Init method'''

# __init__ is called automatically when a new instance is constructed
# __init__ is the constructor of the class

class MyNum(object):
    '''My Num'''
    def __init__(self, val):
        try:
            val = int(val)
        except ValueError:
            val = 0
        self.val = val

    def increment(self):
        '''Increments the value'''
        self.val = self.val + 1

MYNUM1 = MyNum(10)
MYNUM1.increment()
MYNUM1.increment()

MYNUM2 = MyNum('as')
MYNUM2.increment()
MYNUM2.increment()

print MYNUM1.val
print MYNUM2.val


