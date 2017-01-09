'''instance attributes'''

#attributes in a class is holds the state of the instance

import random

class MyClass(object):
    '''My Class'''
    def __init__(self):
        self.rand_val = 0

    def dothis(self):
        '''dothis'''
        self.rand_val = random.randint(1, 10)

MYINST = MyClass()
MYINST.dothis()
print MYINST.rand_val
